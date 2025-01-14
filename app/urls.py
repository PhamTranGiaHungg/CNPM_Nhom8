from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # Trang chủ
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name="category"),
    path('detail/', views.detail, name="detail"),
    path('logout/', views.logoutPage, name="logout"),
    path('cart/', views.cart, name="cart"),       # Trang giỏ hàng
    path('checkout/', views.checkout, name="checkout"),  # Trang thanh toán
    path('update_item/', views.updateItem, name="update_item"), # thêm sản phẩm vào giỏ khi nhấn
    
]
