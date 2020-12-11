from django.urls import path
from django.urls import re_path

from application.blog import views
from application.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="index"),
    path("new/", views.NewPostView.as_view()),
    path("dell_all_post/", views.DelAll.as_view()),
    path("post/<int:pk>/", views.SinglePostView.as_view()),
    path("post/<int:pk>/delete/", views.DeletePostView.as_view()),
    path("post/<int:pk>/update/", views.UpdatePostView.as_view()),
]
