from django.shortcuts import render
from django.http import HttpResponse

from .models import Payment


def index(request):
    return HttpResponse("Payment's urls works!...")
