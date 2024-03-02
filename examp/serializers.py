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
        fields = ("product", 'image')


class ProductListAPIView(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    shop = serializers.StringRelatedField(read_only=True)

    # image = serializers.ListSerializer(child=GallerySerializer(), source='image')

    class Meta:
        model = models.Product
        fields = ('id', 'title', 'description', 'price', 'amount', 'is_active', 'category', 'shop',)


class ProductCreateSerializer(serializers.ModelSerializer):
    images = GallerySerializer(many=True, read_only=True)
    upload_images = serializers.ListSerializer(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False), write_only=True)

    class Meta:
        model = models.Product
        fields = (
            'id', 'title', 'description', 'price', 'amount', 'is_active', 'category', 'shop', 'images', "upload_images")

    def create(self, validate_data):
        uploaded_images = validate_data.pop('upload_images')
        product = models.Product.objects.create(**validate_data)

        for item in uploaded_images:
            new_product_image = models.Gallery.objects.create(product=product, image=item)
        return product
