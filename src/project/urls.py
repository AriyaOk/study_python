from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def index(request: HttpRequest) -> HttpResponse:
    result = render(request, "index.html")

    response = HttpResponse(result)

    return response


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
]
