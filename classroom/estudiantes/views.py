from django.shortcuts import render, get_object_or_404
from .models import Estudiante
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import EstudianteSerializer
# Create your views here.

class EstudianteView(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
