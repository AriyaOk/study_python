from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class BlogPost(models.Model):
    title = models.TextField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    crested_at = models.DateTimeField(default=datetime.now)
    nr_likes = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-crested_at"]

    def get_absolute_url(self):
        kwargs = {"pk": self.pk}
        url = reverse_lazy("blog:post", kwargs=kwargs)
        return url



class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

