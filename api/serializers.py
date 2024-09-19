from rest_framework.serializers import ModelSerializer

from phones import models


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'


class PhoneReviewSerializer(ModelSerializer):
    class Meta:
        model = models.PhoneReview
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'