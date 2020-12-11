from django.urls import path
from django.urls import re_path

from application.blog import views
from application.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="all"),
    path("new/", views.NewPostView.as_view(), name="new"),
    path("dell_all_post/", views.DelAll.as_view(),name="dell_all"),
    path("post/<int:pk>/", views.UpdatePostView.as_view(), name="post"),
    path("post/<int:pk>/delete/", views.DeletePostView.as_view(), name="delete"),
]
