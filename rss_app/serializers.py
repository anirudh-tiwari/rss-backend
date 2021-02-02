from rest_framework import serializers
from .models import Link
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["name","url"]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token