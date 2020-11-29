from django.urls import path
from .views import ViewEstudiante, EstudianteView

urlpatterns = [
    path('', ViewEstudiante),
    path('<estudiante_id>/', EstudianteView)
]