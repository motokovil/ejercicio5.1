from django.urls import path
from .views import ViewMateria, MateriaView

urlpatterns = [
    path('', ViewMateria),
    path('<materia_id>', MateriaView)
]