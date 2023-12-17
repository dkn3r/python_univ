from django.shortcuts import render
from .models import bloggers


def home(request):
    return render(request, 'home.html', {'bloggers': bloggers})


def blogger_profiles(request):
    return render(request, 'blogger_profiles.html', {'bloggers': bloggers})


def blogger_details(request, blogger_name):
    blogger = bloggers.get(blogger_name)
    return render(request, 'blogger_details.html', {'blogger': blogger})
