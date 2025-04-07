from rest_framework import serializers
from .models import Category, Place

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']

class PlaceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'address', 'description', 'tags',
            'featured_image', 'bing_maps_url', 'latitude', 'longitude',
            'website', 'phone', 'email', 'social_media',
            'facebook', 'instagram', 'twitter',
            'category', 'category_id', 'created_at'
        ]
