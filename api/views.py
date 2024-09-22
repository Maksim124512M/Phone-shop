from rest_framework.viewsets import ModelViewSet

from phones.models import Phone, PhoneReview, Order

from api.serializers import (
    PhoneSerializer, 
    PhoneReviewSerializer, 
    OrderSerializer
)


class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneReviewViewSet(ModelViewSet):
    queryset = PhoneReview.objects.all()
    serializer_class = PhoneReviewSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
