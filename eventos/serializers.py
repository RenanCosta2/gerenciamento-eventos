from rest_framework import serializers

from .models import Local, Evento, Custo

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = "__all__"

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"

class CustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custo
        fields = "__all__"