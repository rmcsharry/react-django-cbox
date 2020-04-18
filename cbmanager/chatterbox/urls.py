from rest_framework import routers
from .api import OrganisationViewSet, CourseViewSet, StudentViewSet, EnrollmentViewSet, ProgressViewSet
from .views import ActiveEnrollmentsView, OrganisationEnrolledStudentsView, OrganisationEnrolledCoursesView

from django.conf.urls import url

router = routers.DefaultRouter()
router.register('api/v1/organisations', OrganisationViewSet, 'organisation')
router.register('api/v1/courses', CourseViewSet, 'course')
router.register('api/v1/students', StudentViewSet, 'student')
router.register('api/v1/enrollments', EnrollmentViewSet, 'enrollment')
router.register('api/v1/progress', ProgressViewSet, 'progress')
router.register('api/v1/activeenrollments', ActiveEnrollmentsView, 'active')

# The below exposes: /api/v1/organisations/1/students/
router.register('api/v1/organisations/(?P<organisation_pk>\d+)/students', OrganisationEnrolledStudentsView, 'organisation students')
# The below exposes: /api/v1/organisations/1/courses/
router.register('api/v1/organisations/(?P<organisation_pk>\d+)/courses', OrganisationEnrolledCoursesView, 'organisation courses')

urlpatterns = router.urls
