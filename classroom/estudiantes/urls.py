from django.urls import path
from .views import EstudianteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', EstudianteView)

urlpatterns = router.urls