from django.db import models
from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=256)
    description = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.title


class Shop(BaseModel):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to="shop/")

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop")

    def __str__(self):
        return self.title

    def get_first_photo(self):
        if self.product:
            try:
                return self.product.first().image.url
            except:
                return '-'
        else:
            return '-'


class Gallery(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product", editable=False)
    image = models.ImageField(upload_to="product/")
