from rest_framework import generics, filters, views
from rest_framework.permissions import IsAuthenticated
from examp import models, serializers, permissions
from django.http import HttpResponse
from users.models import User


class ShopListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = [permissions.IsShopAdminPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ('title',)


class ShopRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = [permissions.IsShopAdminPermission]


class ShopDeleteAPIView(views.APIView):
    permission_classes = [permissions.IsShopAdminPermission]

    def get_object(self, pk):
        obj = models.Shop.objects.get(pk=pk)
        return obj

    def delete(self, request, pk):
        queryset = self.get_object(pk=pk)
        queryset.delete()
        return HttpResponse("O'chirildi")


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsCategoryAdminPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ('id', 'title', 'children')


class CategoryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Category.objects.all()
    permission_classes = [permissions.IsCategoryAdminPermission]
    serializer_class = serializers.CategorySerializer


class CategoryDeleteAPIView(views.APIView):
    permission_classes = [permissions.IsCategoryAdminPermission]

    def get_object(self, pk):
        return models.Category.objects.get(pk=pk)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return HttpResponse("O'chirildi")


class ProductListAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListAPIView
    permission_classes = [permissions.IsProductAdminPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('id', "title")


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = models.Product.objects.all()
    # permission_classes = [permissions.IsProductAdminPermission]
    serializer_class = serializers.ProductCreateSerializer


class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Product.objects.all()
    permission_classes = [permissions.IsProductAdminPermission]
    serializer_class = serializers.ProductCreateSerializer


class ProductDeleteAPIView(views.APIView):
    permission_classes = [permissions.IsProductAdminPermission]

    def get_object(self, pk):
        return models.Product.objects.get(pk=pk)

    def delete(self, pk):
        queryset = self.get_object(pk=pk)
        queryset.delete()
        return HttpResponse("O'chirildi")
