from rest_framework import serializers

from sales_network.models import NetworkElement, Product
from sales_network.validators import DebtChangeValidator


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели Product"""
    class Meta:
        model = Product
        fields = '__all__'


class NetworkElementSerializer(serializers.ModelSerializer):
    """Сериализатор модели NetworkElement"""
    class Meta:
        model = NetworkElement
        fields = '__all__'


class NetworkElementUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор модели NetworkElement для обновления, исключающий возможность изменять задолженность через API"""
    class Meta:
        model = NetworkElement
        fields = '__all__'
        validators = [
            DebtChangeValidator(debt='debt',)
        ]
