from django.shortcuts import render, get_object_or_404
from .models import Estudiante
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EstudianteSerializer
# Create your views here.

@api_view(['GET','POST'])
def ViewEstudiante(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        serialized = EstudianteSerializer(estudiantes, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )
    if request.method == 'POST':
        estudiantes = EstudianteSerializer(data=request.data)
        if estudiantes.is_valid():
            estudiantes.save()
            return Response(
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=estudiantes.errors,
            )

@api_view(['GET','PUT','DELETE'])
def EstudianteView(request, estudiante_id):
    
    estudiante = get_object_or_404(Estudiante,id=estudiante_id)
    if request.method == 'GET':
        serialized = EstudianteSerializer(estudiante)
        return Response(
            status=status.HTTP_200_OK, data=serialized.data
        )
    if request.method == 'PUT':
        serialized = EstudianteSerializer(instance=estudiante, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if request.method == 'DELETE':
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    