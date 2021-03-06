from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from django.utils import timezone

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories"

    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url=models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    