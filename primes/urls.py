from django.urls import path, include
from .views import FetchPrimeNumbers

urlpatterns = [
    path("", FetchPrimeNumbers.as_view(), name='fetch_prime'),
]
