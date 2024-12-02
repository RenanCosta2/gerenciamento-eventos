from rest_framework import serializers

from .models import Local, Evento, Custo

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = "__all__"
        read_only_fields = ['usuario']

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"
        read_only_fields = ['usuario']

    def validate(self, data):
        if data['dataFim'] < data['dataInicio']:
            raise serializers.ValidationError("A data de término não pode ser antes da data de início.")
        return data

class CustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custo
        fields = "__all__"