from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Local, Evento, Custo
from .serializers import LocalSerializer, EventoSerializer, CustoSerializer

class LocalViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Local.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Evento.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class CustoViewSet(viewsets.ModelViewSet):
    serializer_class = CustoSerializer
    queryset = Custo.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Custo.objects.filter(evento__usuario=self.request.user)