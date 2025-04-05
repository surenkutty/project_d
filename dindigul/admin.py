from django.contrib import admin
from .models import Category, Place

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="40" height="40" style="object-fit: cover;" />'
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = 'Logo'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address_short', 'phone', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'address', 'tags', 'description')
    readonly_fields = ('created_at',)
    
    def address_short(self, obj):
        return obj.address[:50] + '...' if len(obj.address) > 50 else obj.address
    address_short.short_description = 'Address'


# Register your models here.
