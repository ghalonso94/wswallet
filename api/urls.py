from django.urls import path, include
from . import views
from .views import CompanyViewSet, CustomerViewSet, SaleViewSet, SaleItemViewSet, CashbackViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="WS Wallet",
        default_version='v1',
        description="API Rest to generate and register cashbacks for all partners companies of WS Wallet",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@wswallet.com"),
        license=openapi.License(name="BSD License"),
    ),

    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='Company')
router.register('customer', CustomerViewSet, basename='Customer')
router.register('sale', SaleViewSet, basename='Sale')
router.register('saleitem', SaleItemViewSet, basename='SaleItem')
router.register('cashback', CashbackViewSet, basename='Cashback')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]