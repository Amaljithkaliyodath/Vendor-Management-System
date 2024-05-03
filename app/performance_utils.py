from django.utils import timezone
from django.db.models import F
from .models import Vendor, PurchaseOrder

def update_performance_metrics(vendor):
    purchase_orders = vendor.purchase_orders.all()
    total_orders = purchase_orders.count()
    if total_orders > 0:
        on_time_deliveries = purchase_orders.filter(status='completed', delivery_date__gte=F('issue_date')).count()
        vendor.on_time_delivery_rate = on_time_deliveries / total_orders

        quality_ratings = [po.quality_rating for po in purchase_orders.filter(status='completed', quality_rating__isnull=False)]
        if quality_ratings:
            vendor.quality_rating_avg = sum(quality_ratings) / len(quality_ratings)

        response_times = [po.acknowledgment_date - po.issue_date for po in purchase_orders.filter(acknowledgment_date__isnull=False)]
        if response_times:
            vendor.average_response_time = sum(response_times, timezone.timedelta()) / len(response_times)

        fulfilled_orders = purchase_orders.filter(status='completed').exclude(quality_rating__isnull=True).count()
        vendor.fulfillment_rate = fulfilled_orders / total_orders

    vendor.save()