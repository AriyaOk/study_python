from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from application.blog.models import BlogPost


def index(request):
    context = {
        "object_list" :  BlogPost.objects.all()
    }
    response = render(request, "blog/index.html", context=context)
    return response
