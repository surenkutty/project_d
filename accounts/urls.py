from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegistrationView,LoginView,UserProfileView

router = DefaultRouter()
router.register('register',RegistrationView,basename='register')
router.register('login',LoginView,basename='login')


urlpatterns = [
    path('',include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]