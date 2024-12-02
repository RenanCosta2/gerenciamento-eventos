from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'first_name', 'last_name', 'cpf', 'email', 'password'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user