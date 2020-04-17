from rest_framework import serializers
from .models import Organisation, Course, Student
import datetime
from django.utils.timezone import make_aware

# Organisation Serializer
class OrganisationSerializer(serializers.ModelSerializer):
  students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')

  class Meta:
    model = Organisation
    fields = ('id', 'name', 'students')

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'


    # Student Serializer
class StudentSerializer(serializers.ModelSerializer):
  organisation = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='organisation-detail')
  class Meta:
    model = Student
    fields = ('id', 'first_name', 'last_name', 'email', 'organisation')
