from django.urls import path
from theme.views import landingPage

urlpatterns = [
    path('landingpage/', landingPage, name="landingpage")
]
