from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
