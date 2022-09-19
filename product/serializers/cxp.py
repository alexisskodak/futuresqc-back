from rest_framework import serializers

from product.models import Cxp as ProductFeature
from product.models import Productos


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = "__all__"


class ProductFeatureSerializer(serializers.ModelSerializer):
    productoid = serializers.PrimaryKeyRelatedField(queryset=Productos.objects.all())

    class Meta:
        model = ProductFeature
        fields = "__all__"
