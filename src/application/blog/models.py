from datetime import datetime

from django.db import models


class BlogPost(models.Model):
    title = models.TextField(null=True, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    crested_at = models.DateTimeField(default=datetime.now)
    nr_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["-crested_at"]
