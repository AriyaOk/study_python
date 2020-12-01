from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


def index(request):
    response = render(request, "blog/index.html")
    return response
