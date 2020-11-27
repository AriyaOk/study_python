from django.urls import path

from application.hello import views


urlpatterns = [
    path("", views.view_hello_index),
    path("hello/", views.view_hello_greet),
    path("h_del/", views.view_hello_reset),
]
