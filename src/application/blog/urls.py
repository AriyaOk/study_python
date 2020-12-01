from django.urls import path

from application.blog.views import index

urlpatterns = [
    path("", index),
]
