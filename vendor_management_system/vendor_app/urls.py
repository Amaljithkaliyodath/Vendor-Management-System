

from django.urls import path
from. import views  # Import views from the same directory

urlpatterns = [
    path('vendor/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),
    path('purchase_order/<int:po_id>/', views.purchase_order_detail, name='purchase_order_detail'),
    path('historical_performance/<int:vendor_id>/', views.historical_performance_detail, name='historical_performance_detail'),
]
