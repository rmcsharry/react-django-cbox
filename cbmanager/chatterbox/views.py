from .models import Enrollment, Student, Organisation, Course
from .serializers import EnrollmentSerializer, StudentSerializer, CourseSerializer
from rest_framework import mixins, viewsets
import datetime
from django.utils.timezone import make_aware

class ActiveEnrollmentsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
  # """
  # Returns active enrollments
  # (those who have a booking in past 30 days)
  # """
  serializer_class = EnrollmentSerializer
  queryset = Enrollment.objects.filter(is_active=True)

class OrganisationEnrolledStudentsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
  serializer_class = StudentSerializer

  def get_queryset(self):
    org_id = self.kwargs['organisation_pk']
    qs = Student.objects.get_enrolled_students(org_id)
    return qs

class OrganisationEnrolledCoursesView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
  serializer_class = CourseSerializer

  def get_queryset(self):
    org_id = self.kwargs['organisation_pk']
    qs = Course.objects.get_enrolled_courses(1)
    return qs
