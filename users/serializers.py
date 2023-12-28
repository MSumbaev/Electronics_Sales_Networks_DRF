from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User"""
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор модели User для регистрации"""
    class Meta:
        model = User
        fields = ('username', 'password')
