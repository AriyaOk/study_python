from django import template

from application.blog.models import BlogPost
from application.blog.models import UserLike

register = template.Library()


@register.simple_tag
def is_user_like_(user, post):
    try:
        userlike = UserLike.objects.get(user=user, post=post)
    except UserLike.DoesNotExist:
        return "class=nolikes"
    else:
        return "class=likes"


@register.simple_tag
def nr_likes(post):
    userlike = UserLike.objects.filter(post=post)
    return str(userlike.count())
