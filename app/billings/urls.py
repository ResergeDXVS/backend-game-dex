from django.urls import path
from .views import APIBilling

urlpatterns = [
    path('billing/',APIBilling.as_view()),
]