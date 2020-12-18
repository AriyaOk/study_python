from django import template

from application.blog.models import BlogPost
from application.blog.models import UserLike

register = template.Library()


@register.simple_tag
def total_posts(user, post):
    try:
        userlike = UserLike.objects.get(user=user, post=post)
    except UserLike.DoesNotExist:
        return "class=nolikes"
    else:
        return "class=likes"
