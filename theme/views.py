from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def homePage(request):
    context = {}
    return render(request, 'base.html', context)

def landingPage(request):
    context = {}
    return render(request, 'base.html', context)

def eventsPage(request):
    context = {}
    return render(request, 'events.html', context)

def membershipPage(request):
    context = {}
    return render(request, 'membership.html', context)

def helpPage(request):
    context = {}
    return render(request, 'help.html', context)