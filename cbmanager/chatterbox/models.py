from django.db import models
from model_utils.models import TimeStampedModel
from datetime import datetime as DateTime, timedelta as TimeDelta, date as Date
from django.db.models import Case, When, Value, F, ExpressionWrapper

class Organisation(TimeStampedModel):
  objects = models.Manager()
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)
      
class Student(TimeStampedModel):
  objects = models.Manager()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  organisation = models.ForeignKey(to=Organisation, on_delete=models.SET_NULL, default=None, null=True, related_name='students')

  def __str__(self):
    return self.email

  class Meta:
      ordering = ('last_name','first_name')

class Course(TimeStampedModel):
  objects = models.Manager()
  language = models.CharField(max_length=30)
  level = models.CharField(max_length=2)

  def __str__(self):
    return self.language + ' ' + self.level

  class Meta:
    unique_together = ('language', 'level')
    ordering = ('language','level')

class EnrollmentCustomQuerySet(models.QuerySet):
  # These are somewhat superfluous, but kind of useful wrappers/helpful methods
  def org_students_current(self, organisation):
    return self.filter(student__organisation__id=organisation).filter(is_current=True)
  def org_students_lapsed(self, organisation):
    return self.filter(student__organisation__id=organisation).filter(is_current=False)

class EnrollmentManager(models.Manager.from_queryset(EnrollmentCustomQuerySet)):
  # allow 1 extra day beyond 26 weeks for calculating when an enrollment ends
  # because midnight is actually the start of a new day, not the end
  # (and also because of leap years!)
  COURSE_DURATION = TimeDelta(days=183)

  def get_queryset(self):
      """Overrides the models.Manager method"""
      current_lookback = DateTime.today() - self.COURSE_DURATION
      active_lookback = DateTime.today() - TimeDelta(days=45)
      qs = super(EnrollmentManager, self).get_queryset().annotate(
        end_date=ExpressionWrapper(
            F('enrolled') + TimeDelta(days=182),
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

  class Meta:
    ordering = ('enrolled',)

class Progress(TimeStampedModel):
  objects = models.Manager()
  organisation = models.ForeignKey(to=Organisation, on_delete=models.DO_NOTHING, default=None, null=False)
  course = models.ForeignKey(to=Course, on_delete=models.DO_NOTHING, default=None, null=False)
  calculated_date = models.DateField(default=Date.today)
  ontrack = models.IntegerField(default=0, null=False)
  slow = models.IntegerField(default=0, null=False)
  inactive = models.IntegerField(default=0, null=False)
  lapsed = models.IntegerField(default=0, null=False)

  # Protects against running expensive calcualtions more than once a day
  # (forces you to explicitly delete the existing data for a given calcualted_date)
  class Meta:
    unique_together = ('calculated_date', 'organisation', 'course')