# Generated by Django 4.2.7 on 2024-02-25 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                (
                    "description",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="children", to="examp.category"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="shop/")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=12, max_digits=12)),
                ("amount", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="category", to="examp.category"
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="shop", to="examp.shop"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="product/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="product", to="examp.product"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]