from rest_framework import mixins, viewsets

from product.models import Productos as Product
from product.serializers import ProductSerializer


class ProductViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
