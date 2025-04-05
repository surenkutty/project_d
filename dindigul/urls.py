from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
