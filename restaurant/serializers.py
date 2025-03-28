from rest_framework import serializers
from django.contrib.auth.models import User
from .models import menu, booking


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = "__all__"


class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = "__all__"


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
