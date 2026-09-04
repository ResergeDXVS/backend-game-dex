from django.urls import path, include
from .views import GetProductDetail,GetProductListMainPage,GetProductList,GetCompanies


urlpatterns = [
    path('get-product-detail/<int:pk>/', GetProductDetail.as_view()),
    path('get-product-list-main/',GetProductListMainPage.as_view()),
    path('get-product-list-category/<str:category>/',GetProductList.as_view()),
    path('get-companies/',GetCompanies.as_view()),
]