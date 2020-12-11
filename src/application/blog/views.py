from os.path import basename
from os.path import normpath
from typing import Dict

from django import forms
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic import ListView
from django.views.generic import RedirectView

from application.blog.models import BlogPost
from framework.mixins import ExtendedContextMixin


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(attrs={"rows": 2}),
        }


class AllPostsView(ExtendedContextMixin, ListView):
    template_name = "blog/all_posts.html"
    model = BlogPost

    def get_extended_context(self) -> Dict:
        context = {"form": PostForm()}

        return context


class NewPostView(CreateView):
    http_method_names = ["post"]
    model = BlogPost
    fields = ["content", "title"]
    success_url = reverse_lazy("blog:all")


class DelAll(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        BlogPost.objects.all().delete()
        return reverse_lazy("blog:all")


class SinglePostView(DetailView):
    fields = ["content", "title"]
    template_name = "blog/post.html"
    model = BlogPost

class DeletePostView(DeleteView):
    http_method_names = ["post"]
    model = BlogPost
    success_url = reverse_lazy("blog:all")

class UpdatePostView(UpdateView):
    model = BlogPost
    fields = ["content", "title"]
    template_name = "blog/post.html"
    success_url = reverse_lazy("blog:all")







