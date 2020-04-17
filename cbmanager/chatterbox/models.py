from django.db import models
from model_utils.models import TimeStampedModel
import datetime as dt
from django.db.models import Case, When, Value, F, ExpressionWrapper

class Organisation(TimeStampedModel):
  objects = models.Manager()
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Student(TimeStampedModel):
  objects = models.Manager()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  organisation = models.ForeignKey(to=Organisation, on_delete=models.SET_NULL, default=None, null=True, related_name='students')

  def __str__(self):
    return self.email

class Course(TimeStampedModel):
  objects = models.Manager()
  language = models.CharField(max_length=30)
  level = models.CharField(max_length=2)

  def __str__(self):
    return self.language + ' ' + self.level

  class Meta:
    unique_together = ('language', 'level')

class EnrollmentCustomQuerySet(models.QuerySet):
  def org_students_current(self, organisation):
    return self.filter(student__organisation__id=organisation).filter(is_current=True)
  def org_students_active(self, organisation):
    return self.filter(student__organisation__id=organisation).filter(is_active=True)

class EnrollmentManager(models.Manager.from_queryset(EnrollmentCustomQuerySet)):
  COURSE_DURATION = dt.timedelta(days=183) # allow one extra day beyond 26 weeks

  def get_queryset(self):
      """Overrides the models.Manager method"""
      current_lookback = dt.datetime.today() - self.COURSE_DURATION
      active_lookback = dt.datetime.today() - dt.timedelta(days=30)
      qs = super(EnrollmentManager, self).get_queryset().annotate(
        end_date=ExpressionWrapper(
            F('enrolled') + dt.timedelta(days=182),
            output_field=models.DateField(),
        ),
        is_current=Case(
            When(
                enrolled__gte=current_lookback,
                then=Value(True)
            ),
            default=Value(False),
            output_field=models.BooleanField()
        ),
        is_active=Case(
            When(
                last_booking__gte=active_lookback,
                then=Value(True)
            ),
            default=Value(False),
            output_field=models.BooleanField()
        ))
      return qs

class Enrollment(TimeStampedModel):
  objects = EnrollmentManager()
  course = models.ForeignKey(to=Course, on_delete=models.CASCADE, default=None, null=False, related_name='courses')
  student = models.ForeignKey(to=Student, on_delete=models.CASCADE, default=None, null=False, related_name='enrollments')
  enrolled = models.DateField()
  last_booking = models.DateField()
  credits_total = models.SmallIntegerField(default=10)
  credits_balance = models.DecimalField(max_digits=5, decimal_places=2)
