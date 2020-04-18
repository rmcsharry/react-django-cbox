import logging
import decimal
from datetime import datetime as DateTime, timedelta as TimeDelta, date as Date
from django.db.models.functions import TruncDate
from django.core.management.base import BaseCommand

from chatterbox.models import Organisation, Course, Student, Enrollment, Progress
from chatterbox.views import ActiveEnrollmentsView
from chatterbox.api import EnrollmentSerializer

class Command(BaseCommand):

    # TODO: Make the org a parameter to the command

    def store_active(cls, course, on_track, slow):
      progress, _ = Progress.objects.get_or_create(
        organisation_id=1,
        course=course,
      )
      progress.on_track += on_track
      progress.slow += slow
      progress.save()

    def store_inactive(self, course):
      progress, _ = Progress.objects.get_or_create(
        organisation_id=1,
        course=course,
      )
      progress.inactive += 1
      progress.save()

    def store_lapsed(self, course):
      progress, _ = Progress.objects.get_or_create(
        organisation_id=1,
        course=course,
      )
      progress.lapsed += 1
      progress.save()

    def handle(self, **options):
      org_id = 1
      Progress.objects.filter(organisation_id=org_id, calculated_date=Date.today()).delete()
      logger = logging.getLogger('commands') #from LOGGING.loggers in settings.py
      
      # Process current enrollments that are ACTIVE
      active = Enrollment.objects.org_students_current(org_id).filter(is_active=True)
      on_track = 0
      slow = 0
      logger.info(f'Calculating progress for AEKI - {active.count()} current & active students')
      for enrollment in active:
        student = enrollment.student
        # number of credits converted to days that the student has available to complete the course
        days_remaining = enrollment.credits_balance * decimal.Decimal('18.2')
        # number of days available until enrollment expires
        days_available = (enrollment.end_date - Date.today()).days
        logger.info(f'{DateTime.now()}: Processing student {student.id} - {days_remaining} days remaining - {days_available} days available')
        if days_available >= days_remaining:
          on_track += 1
          self.store_active(enrollment.course, 1, 0)
        else:
          slow += 1
          self.store_active(enrollment.course, 0, 1)
      
      # Process current enrollments that are INACTIVE
      inactive = Enrollment.objects.org_students_current(org_id).filter(is_active=False)
      for enrollment in inactive:
        self.store_inactive(enrollment.course)

      # Process students whose enrollments have LAPSED
      lapsed = Enrollment.objects.filter(student__organisation_id=org_id, is_current=False)
      for enrollment in lapsed:
        self.store_lapsed(enrollment.course)

      logger.info(f'{DateTime.now()}: ON TRACK: {on_track}')
      logger.info(f'{DateTime.now()}: SLOW: {slow}')
      logger.info(f'{DateTime.now()}: INACTIVE: {inactive.count()}')
      logger.info(f'{DateTime.now()}: LAPSED: {lapsed.count()}')

      return "DONE"
