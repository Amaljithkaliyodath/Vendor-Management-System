from django.shortcuts import render
from.models import Vendor, PurchaseOrder, HistoricalPerformance

def vendor_detail(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    return render(request, 'vendor_detail.html', {'vendor': vendor})

def purchase_order_detail(request, po_id):
    po = PurchaseOrder.objects.get(id=po_id)
    return render(request, 'purchase_order_detail.html', {'po': po})

def historical_performance_detail(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    performances = HistoricalPerformance.objects.filter(vendor=vendor).order_by('-date')
    return render(request, 'historical_performance_detail.html', {'performances': performances})
