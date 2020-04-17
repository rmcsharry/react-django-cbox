from rest_framework import serializers
from .models import Organisation, Course, Student, Enrollment
import datetime
from django.utils.timezone import make_aware

class OrganisationSerializer(serializers.ModelSerializer):
  students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')

  class Meta:
    model = Organisation
    fields = ('id', 'name', 'students')

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
  student = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='student-detail')
  course = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='course-detail')
  end_date = serializers.SerializerMethodField()
  is_active = serializers.SerializerMethodField()
  is_current = serializers.SerializerMethodField()

  class Meta:
    model = Enrollment
    fields = ('id', 'enrolled', 'student', 'course', 'end_date', 'is_current', 'last_booking', 'is_active', 'credits_balance')

  def get_end_date(self, obj):
    return obj.end_date

  def get_is_active(self, obj):
    return obj.is_active

  def get_is_current(self, obj):
    return obj.is_current

class StudentSerializer(serializers.ModelSerializer):
  enrollments = EnrollmentSerializer(many=True, read_only=True)
  organisation = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='organisation-detail')
  class Meta:
    model = Student
    fields = ('id', 'first_name', 'last_name', 'email', 'organisation', 'enrollments')
