from django.urls import path

from application.blog import views

urlpatterns = [
    path("", views.index),
    path("new/", views.create_new),
    path("dell_all_post/", views.del_all),
]
