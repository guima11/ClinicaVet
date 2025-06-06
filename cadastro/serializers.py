from rest_framework import serializers
from .models import Vet, Tutor, Cadastro

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'
