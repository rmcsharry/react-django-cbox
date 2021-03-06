from .models import Organisation, Course, Student, Enrollment, Progress
from rest_framework import viewsets, permissions
from .serializers import OrganisationSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer, ProgressSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date as Date

# Organisation Viewset
class OrganisationViewSet(viewsets.ModelViewSet):
  queryset = Organisation.objects.all()
  serializer_class = OrganisationSerializer
  permission_classes = [
    permissions.AllowAny
  ]

# Course Viewset
class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  permission_classes = [
    permissions.AllowAny
  ]

# Student Viewset
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [
    permissions.AllowAny
  ]

# Enrollment Viewset
class EnrollmentViewSet(viewsets.ModelViewSet):
  queryset = Enrollment.objects.all()
  serializer_class = EnrollmentSerializer
  permission_classes = [
    permissions.AllowAny
  ]

# Progress Viewset
class ProgressViewSet(viewsets.ModelViewSet):
  queryset = Progress.objects.filter(calculated_date=Date.today())
  serializer_class = ProgressSerializer
  permission_classes = [
    permissions.AllowAny
  ]