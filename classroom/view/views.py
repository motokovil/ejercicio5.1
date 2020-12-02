from .models import View
from .serializers import ViewSerializer

from rest_framework import viewsets

# Create your views here.

class ElView(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer



