from rest_framework import routers
from .api import OrganisationViewSet, CourseViewSet, StudentViewSet, EnrollmentViewSet, ProgressViewSet
from .views import ActiveEnrollmentsView, OrganisationEnrolledStudentsView, OrganisationEnrolledCoursesView

from django.conf.urls import url

router = routers.DefaultRouter()
router.register('v1/organisations', OrganisationViewSet, 'organisation')
router.register('v1/courses', CourseViewSet, 'course')
router.register('v1/students', StudentViewSet, 'student')
router.register('v1/enrollments', EnrollmentViewSet, 'enrollment')
router.register('v1/progress', ProgressViewSet, 'progress')
router.register('v1/activeenrollments', ActiveEnrollmentsView, 'active')

# The below exposes: //v1/organisations/1/students/
router.register('v1/organisations/(?P<organisation_pk>\d+)/students', OrganisationEnrolledStudentsView, 'organisation students')
# The below exposes: //v1/organisations/1/courses/
router.register('v1/organisations/(?P<organisation_pk>\d+)/courses', OrganisationEnrolledCoursesView, 'organisation courses')

urlpatterns = router.urls
