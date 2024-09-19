from rest_framework.routers import SimpleRouter

from api.views import PhoneViewSet, PhoneReviewViewSet, OrderViewSet


app_name = 'api'

router = SimpleRouter()
router.register(r'phones', PhoneViewSet)
router.register(r'reviews', PhoneReviewViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = router.urls