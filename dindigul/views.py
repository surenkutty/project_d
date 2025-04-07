from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .models import Place, Category
from .serializers import PlaceSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(detail=True, methods=['get'])
    def places(self, request, pk=None):
        category = self.get_object()
        places = category.places.all()  # via related_name
        serializer = PlaceSerializer(places, many=True, context={'request': request})
        return Response(serializer.data)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'description', 'tags', 'category__name']
    ordering_fields = ['name', 'created_at']

