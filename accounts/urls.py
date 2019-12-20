from django.urls import path
from . import views

urlpatterns = [
    # users
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDeatilView.as_view(), name='user-detail'),
    # carts
    path('users/carts/', views.CartListView.as_view(), name='cart-list'),
    path('users/carts/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),
]