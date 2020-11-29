from django.shortcuts import render, get_object_or_404
from .models import Materia
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MateriaSerializer
# Create your views here.

@api_view(['GET','POST'])
def ViewMateria(request):
    if request.method == 'GET':
        materias = Materia.objects.all()
        serialized = MateriaSerializer(materias, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )
    if request.method == 'POST':
        materias = MateriaSerializer(data=request.data)
        if materias.is_valid():
            materias.save()
            return Response(
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=materias.errors,
            )

@api_view(['GET','PUT','DELETE'])
def MateriaView(request, materia_id):
    
    materia = get_object_or_404(Materia,id=materia_id)
    if request.method == 'GET':
        serialized = MateriaSerializer(materia)
        return Response(
            status=status.HTTP_200_OK, data=serialized.data
        )
    if request.method == 'PUT':
        serialized = MateriaSerializer(instance=materia, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if request.method == 'DELETE':
        materia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    