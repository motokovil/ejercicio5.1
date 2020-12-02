from .views import MateriaView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MateriaView)

urlpatterns = router.urls