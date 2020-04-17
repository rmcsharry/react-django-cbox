from rest_framework import routers
from .api import OrganisationViewSet, CourseViewSet, StudentViewSet

from django.conf.urls import url

router = routers.DefaultRouter()
router.register('api/v1/organisations', OrganisationViewSet, 'organisation')
router.register('api/v1/courses', CourseViewSet, 'course')
router.register('api/v1/students', StudentViewSet, 'student')

urlpatterns = router.urls
