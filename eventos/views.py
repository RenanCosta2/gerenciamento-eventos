# Importações do Django REST framework
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

# Importações locais
from .models import Local, Evento, Custo
from .serializers import LocalSerializer, EventoSerializer, CustoSerializer

class LocalViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de Locais
    
    Fornece operações CRUD para locais, com acesso restrito ao usuário proprietário.
    """
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retorna apenas locais do usuário autenticado"""
        return Local.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        """Associa o usuário autenticado ao local durante a criação"""
        serializer.save(usuario=self.request.user)

class EventoViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de Eventos
    
    Fornece operações CRUD para eventos, com acesso restrito ao usuário proprietário.
    """
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retorna apenas eventos do usuário autenticado"""
        return Evento.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        """Associa o usuário autenticado ao evento durante a criação"""
        serializer.save(usuario=self.request.user)

    @action(detail=True, methods=['GET'], url_path="custos")
    def calcular_custos(self, request, pk=None):
        """Endpoint personalizado para calcular custos totais do evento
        
        Retorna uma lista de custos e o valor total acumulado.
        """
        evento = self.get_object()
        if evento:
            custos = Custo.objects.filter(evento=evento)
            total = sum(custo.valor for custo in custos)
            custo_serializer = CustoSerializer(custos, many=True, context={'request': request})

            return Response(
                {'custos': custo_serializer.data, 'total': total}, 
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Evento não encontrado.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

class CustoViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de Custos
    
    Fornece operações CRUD para custos, com acesso restrito aos custos
    dos eventos do usuário autenticado.
    """
    serializer_class = CustoSerializer
    queryset = Custo.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retorna apenas custos dos eventos do usuário autenticado"""
        return Custo.objects.filter(evento__usuario=self.request.user)