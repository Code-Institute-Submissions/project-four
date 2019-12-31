from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart_view, name="cart"),
	path('add-to-cart/<int:pk>/', views.add_to_cart, name="add-to-cart"),
]

