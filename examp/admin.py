from django.apps import apps
from django.contrib import admin
from django.utils.safestring import mark_safe
from examp import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)

    #
    def has_add_permission(self, request) -> bool:
        if request.user.role.filter(title="Category Admin"):
            return True

    def has_view_permission(self, request, obj=None) -> bool:
        if request.user.role.filter(title="Category Admin"):
            return True

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.role.filter(title="Category Admin"):
            return True


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = models.Gallery
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'get_photo')
    list_filter = ('shop',)
    search_fields = ('title',)
    list_select_related = ("category", "shop")
    autocomplete_fields = ("category",)
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

    # def get_queryset(self, request):
    #     return super().get_queryset(request).select_related("category", "shop",)

    def has_add_permission(self, request) -> bool:
        if request.user.role.filter(title="Product Admin"):
            return True

    def has_view_permission(self, request, obj=None) -> bool:
        if request.user.role.filter(title="Product Admin"):
            return True

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.role.filter(title="Product Admin"):
            return True


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_display_links = ("title",)
    search_fields = ('title',)

    def has_add_permission(self, request) -> bool:
        if request.user.role.filter(title="Shop Admin"):
            return True

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.role.filter(title="Shop Admin"):
            return True

    def has_view_permission(self, request, obj=None) -> bool:
        if request.user.role.filter(title="Shop Admin"):
            return True
