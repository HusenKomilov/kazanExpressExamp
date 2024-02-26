# Generated by Django 4.2.7 on 2024-02-25 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("examp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="examp.category",
            ),
        ),
    ]