from django.shortcuts import render
from django.http import HttpResponse

from .models import Member, MembershipType


def index(request):
    return HttpResponse("Member's urls works!...")
