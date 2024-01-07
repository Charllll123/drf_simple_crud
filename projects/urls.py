from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/project', ProjectViewSet, 'project')

urlpatterns = router.urls