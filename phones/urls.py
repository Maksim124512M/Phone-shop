from django.urls import path

from phones.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home')
]