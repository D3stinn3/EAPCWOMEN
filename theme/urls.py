from django.urls import path
from theme.views import landingPage, eventsPage, membershipPage, helpPage

urlpatterns = [
    path('landingpage/', landingPage, name="landingpage"),
    path('eventspage/', eventsPage, name="eventspage"),
    path('membershippage/', membershipPage, name ="membershippage"),
    path('helppage/', helpPage, name="helppage")
]
