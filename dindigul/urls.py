from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, CategoryViewSet,BulkPlaceUploadView

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('upload-places/', BulkPlaceUploadView.as_view(), name='bulk-place-upload'),
    path('', include(router.urls)),
]
