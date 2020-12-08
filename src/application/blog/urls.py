from django.urls import path
from django.urls import re_path

from application.blog import views

urlpatterns = [
    path("", views.AllPostsView.as_view()),
    path("new/", views.NewPostView.as_view()),
    path("dell_all_post/", views.DelAll.as_view()),
    re_path(r"del_post/\d+/", views.del_post),
    re_path(r"dislike_post/\d+/", views.change_nr_likes),
    re_path(r"like_post/\d+/", views.change_nr_likes),
]
