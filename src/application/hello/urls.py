from django.urls import path

from application.hello.views import view_hello_greet
from application.hello.views import view_hello_index
from application.hello.views import view_hello_reset

urlpatterns = [
    path("", view_hello_index),
    path("greet", view_hello_greet),
    path("h_del", view_hello_reset),
]
