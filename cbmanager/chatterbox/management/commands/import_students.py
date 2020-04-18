import csv
import logging
from datetime import datetime as DateTime
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand
from chatterbox.models import Organisation, Course, Student, Enrollment

"""
Script to import student data in csv format
"""
# TODO: error checks and logging to file

class Command(BaseCommand):
    def handle(self, **options):
      logger = logging.getLogger('commands') #from LOGGING.loggers in settings.py
      CSV_PATH = './students_AEKI.csv'

      logger.info('Deleting existing students...')

      Student.objects.filter(organisation__name__exact="AEKI").delete()

      with open(CSV_PATH) as file:
        file.readline() # skip the header
        csv_reader = csv.reader(file, delimiter=',')
        org = Organisation.objects.filter(name='AEKI')

        logger.info(f'Importing students for Organisation: {org[0].name}')
        counter = 0
        for row in csv_reader:
          enrolled = DateTime.strptime(row[4], '%Y-%m-%d')
          last_booking = DateTime.strptime(row[5], '%Y-%m-%d')
          course = Course.objects.filter(language=row[8],level=row[9])[0]

          # we just assume this will work since we are in charge of the data!
          new_student = Student.objects.create(
              first_name=row[0],
              last_name=row[1],
              email=row[2],
              organisation=org[0],
            )

          Enrollment.objects.create(
            course=course,
            student=new_student,
            enrolled=DateTime.strptime(row[4], '%Y-%m-%d'),
            last_booking=DateTime.strptime(row[5], '%Y-%m-%d'),
            credits_total=row[6],
            credits_balance=row[7],
            )
          counter += 1

      logger.info(f'*** {counter} students imported for {org[0].name} ***')
