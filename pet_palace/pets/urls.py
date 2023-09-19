from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet-palace/', views.home, name='pet-palace'),
    path('pet-palace/shopping-cart/', views.shopping_cart, name="shopping-cart"),
    path('pet-palace/add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('pet-palace/checkout/', views.checkout, name='checkout'),
    path('pet-palace/checkout-success', views.checkout_success, name='checkout-success'),
    path('pet-palace/register/', views.register, name='register'),
    path('pet-palace/login/', views.login_user, name='login'),
    path('pet-palace/logout/', views.logout_user, name='logout'),
    path('pet-palace/<str:category_name>/', views.selected_pet_list, name="selected_pet_list"),
    path('pet-palace/<str:category_name>/<str:pet_name>/', views.selected_pet, name="selected_pet")
]

