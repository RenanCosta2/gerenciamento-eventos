from django.forms import ValidationError
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Local, Evento, Custo
from .serializers import LocalSerializer, EventoSerializer, CustoSerializer

class LocalViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    queryset = Local.objects.all()
    permission_classes = [AllowAny]

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = [AllowAny]

class CustoViewSet(viewsets.ModelViewSet):
    serializer_class = CustoSerializer
    queryset = Custo.objects.all()
    permission_classes = [AllowAny]