from django.urls import path
from django.urls import re_path

from application.blog import views

urlpatterns = [
    path("", views.all_posts_view),
    path("new/", views.create_new),
    path("dell_all_post/", views.del_all),
    re_path(r"del_post/\d+/", views.del_post),
    re_path(r"dislike_post/\d+/", views.change_nr_likes),
    re_path(r"like_post/\d+/", views.change_nr_likes),
]
