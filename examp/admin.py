from django.apps import apps
from django.contrib import admin
from django.utils.safestring import mark_safe
from examp import models


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = models.Gallery
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'get_photo')
    inlines = [GalleryInline]

    def get_photo(self, obj):
        if obj.product:
            try:
                return mark_safe(f"<img src='{obj.product.all()[0].image.url}' width='75'>")
            except:
                return '-'
        else:
            return '-'

    get_photo.short_description = "Mahsulot rasmi"


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
