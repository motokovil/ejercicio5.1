from .views import ProfesorView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProfesorView)

urlpatterns = router.urls