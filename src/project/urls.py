"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import mimetypes

from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

from framework.utils import read_static


def index(request: HttpRequest)->HttpResponse:
    result = render(request, "index.html")

    response = HttpResponse(result)

    return response

def logo(request: HttpRequest)->HttpResponse:
    filename_logo = "ariyaOk.gif"
    payload = read_static(filename_logo)
    type_file_ = mimetypes.guess_type(filename_logo)[0]
    response = HttpResponse(payload, content_type=type_file_)
    return response

def style(request: HttpRequest)->HttpResponse:
    filename_style = "styles.css"
    payload = read_static(filename_style)
    type_file_ = mimetypes.guess_type(filename_style)[0]
    response = HttpResponse(payload, content_type=type_file_)
    return response


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("logo.png/", logo),
    path("xxx/", style),
]
