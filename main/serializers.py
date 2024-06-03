from rest_framework import serializers
from .models import English

class EnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = '__all__'