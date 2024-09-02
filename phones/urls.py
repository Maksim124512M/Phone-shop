from django.urls import path

from phones.views import HomeView, PhoneDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
]