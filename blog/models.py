from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from app import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog')
