from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Place, Category
from .serializers import PlaceSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'description', 'tags', 'category__name']
    ordering_fields = ['name', 'created_at']

