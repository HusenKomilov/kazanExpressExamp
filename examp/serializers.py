from rest_framework import serializers
from examp import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('id', 'title', 'description', 'image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title', 'description')


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = ('product', 'image')


class ProductListAPIView(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    shop = serializers.StringRelatedField(read_only=True)
    # image = serializers.ListSerializer(child=GallerySerializer(), source='image')

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'description', 'price', 'amount', 'is_active', 'category', 'shop',)


class ProductCreateSerializer(serializers.ModelSerializer):
    image = GallerySerializer()

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'description', 'price', 'amount', 'is_active', 'category', 'shop', 'image')

    def create(self, validate_data):
        gallery_detail = validate_data.pop('image', None)
        product = models.Product.objects.create(**gallery_detail)

        for item in gallery_detail:
            item['product'] = product
            GallerySerializer.create(ProductCreateSerializer(), **item)
        return product

    # def update(self, instance, validate_data):
    #     product_image = validate_data.pop('product_image')
    #     instance.title = validate_data.get('title', instance.title)
    #     instance.description = validate_data.get('description', instance.title)
    #     instance.price = validate_data.get('price', instance.title)
    #     instance.amount = validate_data.get('amount', instance.title)
    #     instance.category = validate_data.get('category', instance.title)
    #     instance.shop = validate_data.get('shop', instance.title)
    #     instance.save()
