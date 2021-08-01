from django.urls import path, include
from . import views
from .views import CompanyViewSet, CustomerViewSet, SaleViewSet, SaleItemViewSet, CashbackViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='Company')
router.register('customer', CustomerViewSet, basename='Customer')
router.register('sale', SaleViewSet, basename='Sale')
router.register('saleitem', SaleItemViewSet, basename='SaleItem')
router.register('cashback', CashbackViewSet, basename='Cashback')

urlpatterns = [
    path('v1/', include(router.urls))
]