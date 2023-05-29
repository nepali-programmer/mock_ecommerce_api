from django.urls import path
from .views import pay_for_product

urlpatterns = [
    path('<int:pk>/', pay_for_product),
]
