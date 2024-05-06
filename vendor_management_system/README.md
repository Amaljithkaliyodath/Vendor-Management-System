
## Vendor Management System with Performance Metrics

A Vendor Management System (VMS) built using Django and Django REST Framework. This system manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.
## Features
1.Vendor Profile Management:

.Create, retrieve, update, and delete vendor profiles.

.Calculate and display vendor performance metrics.

2.Purchase Order Tracking:

.Create, retrieve, update, and delete purchase orders.

.Track delivery status, items, quantity, and other details.

3.Vendor Performance Evaluation:

.Calculate performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

.Historical performance tracking for trend analysis.
## Installation

Virtual Environment

It is recommended to use a virtual environment to run this project. To create a virtual environment, run the following command:

```bash
 python -m venv venv
```
    
Install the required packages

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
Run
```bash
python manage.py runserver

```

API
```bash 
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/vendors/ 
http://127.0.0.1:8000/api/vendors/<int:pk>/ 
http://127.0.0.1:8000/api/purchase_orders/
http://127.0.0.1:8000/api/purchase_orders/<int:pk>/ 
http://127.0.0.1:8000/api/historical_performance/ 
http://127.0.0.1:8000/api/vendors/<int:vendor_id>/performance/ 
http://127.0.0.1:8000/api/purchase_orders/<int:pk>/acknowledge/ 
```
## API Endpoints

Vendor

GET /api/vendors/

GET /api/vendors/{vendor_id}/

PUT /api/vendors/{vendor_id}/

DELETE /api/vendors/{vendor_id}/

GET /api/vendors/{vendor_id}/performance/




Purchase Order

POST /api/purchase_orders/

GET /api/purchase_orders/

GET /api/purchase_orders/{po_id}/

PUT /api/purchase_orders/{po_id}/

DELETE /api/purchase_orders/{po_id}/



Vendor Performance

PATCH /api/purchase_orders/{po_id}/acknowledge/
## Login Credentials:

```bash
 username: admin
 password: admin
```
## RTest Suite

To run the test suite, run the following command:

```bash
  python manage.py test
```

