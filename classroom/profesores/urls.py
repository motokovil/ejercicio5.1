from django.urls import path
from .views import ViewProfesor, ProfesorView

urlpatterns = [
    path('', ViewProfesor),
    path('<profesor_id>', ProfesorView)
]