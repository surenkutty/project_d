from rest_framework import serializers
from .models import Category, Place, Offers
from django.utils import timezone

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

class OfferSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()

    def get_is_expired(self, obj):
        return obj.end_date < timezone.now()

    class Meta:
        model = Offers
        fields = [
            'id', 'name', 'slug', 'category', 'category_id',
            'place', 'place_id', 'image', 'start_date',
            'end_date', 'is_active', 'created_at', 'is_expired'
        ]
