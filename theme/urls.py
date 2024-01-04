from django.urls import path
from theme.views import landingPage, eventsPage, membershipPage, helpPage, homePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homePage, name="homepage"),
    path('landingpage/', landingPage, name="landingpage"),
    path('eventspage/', eventsPage, name="eventspage"),
    path('membershippage/', membershipPage, name ="membershippage"),
    path('helppage/', helpPage, name="helppage"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
