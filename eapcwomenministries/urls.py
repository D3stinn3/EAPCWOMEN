from django.urls import path
from eapcwomenministries.views import landingPage, eventsPage, membershipPage, helpPage, homePage

urlpatterns = [
    path('', homePage, name="homepage"),
    path('landingpage/', landingPage, name="landingpage"),
    path('eventspage/', eventsPage, name="eventspage"),
    path('membershippage/', membershipPage, name ="membershippage"),
    path('helppage/', helpPage, name="helppage"),
]
