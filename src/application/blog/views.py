from typing import Dict

from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic.detail import BaseDetailView

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

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class DelAll(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        BlogPost.objects.all().delete()
        return reverse_lazy("blog:all")


class DeletePostView(DeleteView):
    http_method_names = ["post"]
    model = BlogPost
    success_url = reverse_lazy("blog:all")


class PostView(UpdateView):
    model = BlogPost
    fields = ["content", "title"]
    template_name = "blog/post.html"
    success_url = reverse_lazy("blog:all")

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)
