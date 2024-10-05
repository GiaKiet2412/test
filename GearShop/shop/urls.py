from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Chi tiết sản phẩm
]