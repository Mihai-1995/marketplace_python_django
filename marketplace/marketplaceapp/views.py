# in fisierul marketplaceapp\views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're on the marketplace app home.")