from django.urls import path

from phones.views import HomeView, PhoneDetailView, CreateOrder


app_name = 'phones'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('create_order/<int:pk>/', CreateOrder.as_view(), name='create_order'),
]