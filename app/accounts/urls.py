from django.urls import path
from .views import APIUser, APIAddress, APICreditCard, APILogin

urlpatterns = [
    path('login/',APILogin.as_view()),
    path('user/',APIUser.as_view()),
    path('address/',APIAddress.as_view()),
    path('card/',APICreditCard.as_view()),
]