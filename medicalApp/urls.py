from django.urls import path, include
from .views import CompanyViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register("company", CompanyViewSet, basename='company')

urlpatterns = [
    path("", include(router.urls),),

    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
