from django.db import models
from model_utils.models import TimeStampedModel

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

