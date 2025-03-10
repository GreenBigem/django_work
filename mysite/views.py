from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    return HttpResponse(status=201)

def api(request):
    return HttpResponse(status=201)

