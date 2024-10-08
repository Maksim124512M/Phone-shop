from django.urls import path
from django.views.decorators.cache import cache_page

from phones.views import ( 
    HomeView,
    PhoneDetailView,
    CreateOrder,
    add_product_in_basket,
    delete_product_from_basket,
    BasketView,
    ReviewDeleteView,
)


app_name = 'phones'

urlpatterns = [
    path('', cache_page(60*60)(HomeView.as_view()), name='home'),
    path('basket/', cache_page(60*60)(BasketView.as_view()), name='basket'),
    path('phone/<int:pk>/', cache_page(60*60)(PhoneDetailView.as_view()), name='phone_detail'),
    path('create_order/<int:pk>/', CreateOrder.as_view(), name='create_order'),
    path('review/delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('add_product/<int:pk>/', add_product_in_basket, name='add_product_in_basket'),
    path('basket/delete/<int:pk>/', delete_product_from_basket, name='delete_product_from_basket'),
]