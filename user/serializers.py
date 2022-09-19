from rest_framework import serializers

from core.serializers import BaseFsqcSerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(allow_blank=True, write_only=True)

    class Meta:
        model = User
        fields = "__all__"


class SmallUserSerializer(BaseFsqcSerializer):
    usuarioid = serializers.CharField(trim_whitespace=True)
    nombre1 = serializers.CharField(trim_whitespace=True)

    class Meta:
        model = User
        fields = ("usuarioid", "nombre1")
        read_only_fields = ("usuarioid", "nombre1")
