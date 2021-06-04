from django.db.models import fields
from rest_framework import serializers
from .models import Acceleration, Sound
from django.utils import timezone

class AccPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceleration
        fields = '__all__'

class AccCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceleration
        fields = ('count','sleeptime',)

class SoundCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('count','sleeptime',)

class SoundPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = '__all__'

