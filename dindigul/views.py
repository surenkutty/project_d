from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .models import Place, Category,Offers
from .serializers import PlaceSerializer, CategorySerializer,OfferSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.utils import timezone


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


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'place__name', 'category__name']
    ordering_fields = ['start_date', 'end_date']

    def get_queryset(self):
        now = timezone.now()
        return Offers.objects.filter(is_active=True, end_date__gte=now)

    @action(detail=True, methods=['get'])
    def offers(self, request, pk=None):
        place = self.get_object()
        offers = place.offers.filter(is_active=True, end_date__gte=timezone.now())
        serializer = OfferSerializer(offers, many=True, context={'request': request})
        return Response(serializer.data)


class ExpiredOfferViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OfferSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'place__name', 'category__name']
    ordering_fields = ['start_date', 'end_date']

    def get_queryset(self):
        return Offers.objects.filter(is_active=False, end_date__lt=timezone.now())


class BulkPlaceUploadView(APIView):
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = PlaceSerializer(data=request.data, many=True, context={'request': request})
        else:
            return Response({"error": "Expected a list of items."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)