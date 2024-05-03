from django.db import models
from django.utils import timezone
from django.db.models import F
import datetime
from app.models import PurchaseOrder
from .performance_utils import update_performance_metrics


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=7))
    
    # Set issue_date for existing purchase orders to the current date and time
    PurchaseOrder.objects.all().update(issue_date=timezone.now())

 # Or, set issue_date to a specific date and time
    
    specific_date = datetime.datetime(2023, 5, 1, 12, 0, 0, tzinfo=timezone.get_current_timezone())
    PurchaseOrder.objects.all().update(issue_date=specific_date)

    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('acknowledged', 'Acknowledged'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ), default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'PO #{self.po_number} - {self.vendor.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.update_performance_metrics()