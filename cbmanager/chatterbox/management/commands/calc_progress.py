import logging
import decimal
from datetime import datetime as DateTime, timedelta as TimeDelta, date as Date
from django.db.models.functions import TruncDate
from django.db.models import Sum
from django.core.management.base import BaseCommand

from chatterbox.models import Organisation, Course, Student, Enrollment, Progress
from chatterbox.views import ActiveEnrollmentsView
from chatterbox.api import EnrollmentSerializer

# TODO: error checks and logging to file

class Command(BaseCommand):
    help="Calculates, as of today, the progress for all students of a given organisation"

    def add_arguments(self, parser):
      parser.add_argument('org_id', type=int, help='The id of the organisation to process')

    @property
    def logger(self):
        return self._logger

    @property
    def org_id(self):
        return self._org_id

    @property
    def course(self):
      return self._course

    def process_active(self, active):
      for enrollment in active:
        student = enrollment.student
        # number of credits converted to days that the student has available to complete the course
        days_remaining = enrollment.credits_balance * decimal.Decimal('18.2')
        # number of days available until enrollment expires
        days_available = (enrollment.end_date - Date.today()).days
        self.logger.info(f'{DateTime.now()}: Processing student {student.id} - {days_remaining} days remaining - {days_available} days available')
        if days_available >= days_remaining:
          self._course = enrollment.course
          self.store_result(ontrack=1)
        else:
          self._course = enrollment.course
          self.store_result(slow=1)

    def store_result(self, ontrack=0, slow=0, inactive=0, lapsed=0):
      progress, _ = Progress.objects.get_or_create(
        organisation_id=self.org_id,
        course=self.course,
      )
      progress.ontrack += ontrack
      progress.slow += slow
      progress.inactive += inactive
      progress.lapsed += lapsed
      progress.save()
      return progress

    def handle(self, *args, **options):
      self._logger = logging.getLogger('commands')  #from LOGGING.loggers in settings.py
      self.logger.info(options)
      self._org_id=options['org_id']

      # Delete any data from today's previous runs
      Progress.objects.filter(organisation_id=self.org_id, calculated_date=Date.today()).delete()

      # Get the different enrollment status types
      current = Enrollment.objects.org_students_current(self.org_id)
      lapsed = Enrollment.objects.org_students_lapsed(self.org_id)
      active = current.filter(is_active=True)
      inactive = current.filter(is_active=False)
      self.logger.info(f'Calculating progress for organisation {self.org_id} - {current.count()} current & {lapsed.count()} students')

      # Process current enrollments that are ACTIVE
      self.process_active(active)
      
      # Process current enrollments that are INACTIVE
      for enrollment in inactive:
        self._course = enrollment.course
        self.store_result(inactive=1)

      # Process students whose enrollments have LAPSED
      for enrollment in lapsed:
        self._course = enrollment.course
        self.store_result(lapsed=1)

      progress = Progress.objects.filter(organisation_id=self.org_id, calculated_date=Date.today()).aggregate(sum_ontrack = Sum('ontrack'), sum_slow=Sum('slow'))
      self.logger.info(f"{DateTime.now()}: *** CALC PROGRESS SUMMARY ***")
      self.logger.info(f'{DateTime.now()}: ON TRACK: {progress["sum_ontrack"]}')
      self.logger.info(f'{DateTime.now()}: SLOW: {progress["sum_slow"]}')
      self.logger.info(f'{DateTime.now()}: INACTIVE: {inactive.count()}')
      self.logger.info(f'{DateTime.now()}: LAPSED: {lapsed.count()}')
      self.logger.info(f"{DateTime.now()}: *** CALC PROGRESS SUMMARY ***")

      return "\033[01;34mDONE"
