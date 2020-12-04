from os.path import basename
from os.path import normpath

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from application.blog.models import BlogPost


def all_posts_view(request):
    context = {"object_list": BlogPost.objects.all()}
    response = render(request, "blog/index.html", context=context)
    return response


def create_new(request: HttpRequest) -> HttpResponse:
    title = request.POST.get("title")
    content = request.POST.get("content")

    p1 = BlogPost(title=title, content=content)
    p1.save()

    return redirect("/b/")


def del_all(request: HttpRequest) -> HttpResponse:
    BlogPost.objects.all().delete()

    return redirect("/b/")


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
