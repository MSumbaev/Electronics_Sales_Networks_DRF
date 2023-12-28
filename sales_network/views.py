from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from sales_network.models import Product, NetworkElement
from sales_network.permissions import IsAuthor
from sales_network.serializers import ProductSerializer, NetworkElementUpdateSerializer, NetworkElementSerializer


# - - - - - - - - - - -Product- - - - - - - - - - -
class ProductCreateApiView(generics.CreateAPIView):
    """Контроллер для создания объекта Product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_product = serializer.save()
        new_product.author = self.request.user
        new_product.save()


class ProductListApiView(generics.ListAPIView):
    """Контроллер для просмотра списка объектов Product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductRetrieveApiView(generics.RetrieveAPIView):
    """Контроллер для просмотра объекта Product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductUpdateApiView(generics.UpdateAPIView):
    """Контроллер для обновления объекта Product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


class ProductDeleteApiView(generics.DestroyAPIView):
    """Контроллер для удаления объекта Product"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


# - - - - - - - - - - -NetworkElement- - - - - - - - - - -
class NetworkElementCreateApiView(generics.CreateAPIView):
    """Контроллер для создания объекта NetworkElement"""
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_network_element = serializer.save()
        new_network_element.author = self.request.user
        new_network_element.save()


class NetworkElementListApiView(generics.ListAPIView):
    """Контроллер для просмотра списка объектов NetworkElement"""
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class NetworkElementRetrieveApiView(generics.RetrieveAPIView):
    """Контроллер для просмотра объекта NetworkElement"""
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [IsAuthenticated]


class NetworkElementUpdateApiView(generics.UpdateAPIView):
    """Контроллер для обновления объекта NetworkElement"""
    serializer_class = NetworkElementUpdateSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


class NetworkElementDeleteApiView(generics.DestroyAPIView):
    """Контроллер для удаления объекта NetworkElement"""
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]
