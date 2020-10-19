from rest_framework import routers

from .api import TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
