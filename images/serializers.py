from rest_framework import serializers
from .models import AiAnalysisLog


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiAnalysisLog
        fields = '__all__'
