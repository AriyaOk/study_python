from typing import Dict

from django import forms
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from application.blog.models import BlogPost
from application.blog.models import UserLike
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


@method_decorator(csrf_exempt, name="dispatch")
class PostLike(View):
    def get(self, request, *args, **kwargs):
        nr = BlogPost.objects.get(pk=kwargs.get("pk")).nr_likes
        payload = str(nr)
        return HttpResponse(payload, content_type="text/plain")

    def post(self, request, *args, **kwargs):
        payload = {"ok": False, "nr_likes": 0, "is_like": 0, "reason": "unknown reason"}
        try:
            pk = kwargs.get("pk", 0)
            post = BlogPost.objects.get(pk=pk)
            user = self.request.user

        except Exception:
            payload.update({"reason": "post not found"})
        else:
            try:
                userlike = UserLike.objects.get(user=user, post=post)
            except UserLike.DoesNotExist:
                userlike = UserLike(user=user, post=post)
                userlike.save()

                post.nr_likes += 1
                post.save()

                is_like = 1
            else:
                userlike.delete()

                post.nr_likes -= 1
                post.save()
                is_like = 0
            post = BlogPost.objects.get(pk=pk)
            payload.update(
                {
                    "ok": True,
                    "nr_likes": post.nr_likes,
                    "is_like": is_like,
                    "reason": None,
                }
            )

        return JsonResponse(payload)
