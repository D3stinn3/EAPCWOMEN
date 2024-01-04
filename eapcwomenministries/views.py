from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homePage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def landingPage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def eventsPage(request):
    context = {}
    return render(request, 'temp/events.html', context)

def membershipPage(request):
    context = {}
    return render(request, 'temp/membership.html', context)

def helpPage(request):
    context = {}
    return render(request, 'temp/help.html', context)
