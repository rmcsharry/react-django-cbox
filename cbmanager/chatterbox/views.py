from .models import Enrollment, Student, Organisation
from .serializers import EnrollmentSerializer, StudentSerializer
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

# TODO: learn how the following can be used to filter out only those students for a given organisation
class OrganisationStudentsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
  serializer_class = StudentSerializer
  queryset = Student.objects.all()
