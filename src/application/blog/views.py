from os.path import basename
from os.path import normpath
from typing import Dict

from django import forms
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import RedirectView

from application.blog.models import BlogPost
from framework.mixins import ExtendedContextMixin


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": 2})}


class AllPostsView(ExtendedContextMixin, ListView):
    template_name = "blog/index.html"
    model = BlogPost

    def get_extended_context(self) -> Dict:
        context = {"form": PostForm()}

        return context


class NewPostView(CreateView):
    http_method_names = ["post"]
    model = BlogPost
    fields = ["content", "title"]
    success_url = "/b/"


class DelAll(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        BlogPost.objects.all().delete()
        return "/b/"


def del_post(request: HttpRequest) -> HttpResponse:
    path_info = request.path_info
    id = basename(normpath(path_info))
    BlogPost.objects.filter(id=id).delete()

    return redirect("/b/")


def change_nr_likes(request: HttpRequest) -> HttpResponse:
    path_info = request.path_info
    id = basename(normpath(path_info))
    post = BlogPost.objects.get(id=id)
    if path_info.find("dislike_post") != -1:
        post.nr_likes -= 1
    else:
        post.nr_likes += 1
    post.save()

    return redirect("/b/")
