from django.urls import path
from .views import ElView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ElView)

urlpatterns = router.urls