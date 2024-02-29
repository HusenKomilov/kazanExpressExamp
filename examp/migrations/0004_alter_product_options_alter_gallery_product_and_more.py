# Generated by Django 4.2.7 on 2024-02-27 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("examp", "0003_alter_product_price"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name_plural": "Products"},
        ),
        migrations.AlterField(
            model_name="gallery",
            name="product",
            field=models.ForeignKey(
                editable=False, on_delete=django.db.models.deletion.CASCADE, related_name="product", to="examp.product"
            ),
        ),
        migrations.AlterField(
            model_name="shop",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="shop/"),
        ),
    ]