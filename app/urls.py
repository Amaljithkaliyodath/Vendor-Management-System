from django.urls import path, include
from rest_framework import routers
from .views import VendorViewSet, PurchaseOrderViewSet, VendorPerformanceView, AcknowledgePurchaseOrderView

router = routers.DefaultRouter()
router.register('vendors', VendorViewSet, basename='vendor')
router.register('purchase_orders', PurchaseOrderViewSet, basename='purchase_order')

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge_purchase_order'),
]