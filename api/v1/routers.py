from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import refresh_jwt_token, ObtainJSONWebToken
from .viewsets import UserViewSet, PostViewSet, RatioViewSet, ratio_analitics
from .serializers import CustomJWTSerializer


router = DefaultRouter()
router.register('user', UserViewSet)
router.register('post', PostViewSet)
router.register('ratio', RatioViewSet)

urlpatterns = [
    path(r'api-token-auth/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'analitics', ratio_analitics)
]

urlpatterns += router.urls
