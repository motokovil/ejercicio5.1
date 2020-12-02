from .models import Materia
from rest_framework import viewsets
from .serializers import MateriaSerializer
from rest_framework.permissions import (AllowAny, IsAdminUser)

# Create your views here.

class MateriaView(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = (AllowAny, )