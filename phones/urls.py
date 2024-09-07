from django.urls import path

from phones.views import HomeView, PhoneDetailView, CreateOrder, add_product_in_basket, BasketView


app_name = 'phones'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('create_order/<int:pk>/', CreateOrder.as_view(), name='create_order'),
    path('add_product/<int:pk>/', add_product_in_basket, name='add_product_in_basket'),
]