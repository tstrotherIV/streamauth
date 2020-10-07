from django.db import models
from django.contrib.auth.models import User

class StreamEvent(models.Model):
  
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    stream_embed = models.CharField(max_length=1000)
    chat_feed = models.CharField(max_length=1000, default=None, blank=True, null=True)
    deleted = models.BooleanField(default=False)