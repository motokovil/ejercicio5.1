from django.shortcuts import render, get_object_or_404
from .models import Profesor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfesorSerializer
# Create your views here.

@api_view(['GET','POST'])
def ViewProfesor(request):
    if request.method == 'GET':
        profesores = Profesor.objects.all()
        serialized = ProfesorSerializer(profesores, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )
    if request.method == 'POST':
        profesores = ProfesorSerializer(data=request.data)
        if profesores.is_valid():
            profesores.save()
            return Response(
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=profesores.errors,
            )

@api_view(['GET','PUT','DELETE'])
def ProfesorView(request, profesor_id):
    
    profesor = get_object_or_404(Profesor,id=profesor_id)
    if request.method == 'GET':
        serialized = ProfesorSerializer(profesor)
        return Response(
            status=status.HTTP_200_OK, data=serialized.data
        )
    if request.method == 'PUT':
        serialized = ProfesorSerializer(instance=profesor, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if request.method == 'DELETE':
        profesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    