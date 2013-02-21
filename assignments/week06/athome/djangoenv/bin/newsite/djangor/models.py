from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def published_today(self):
        now = timezone.now()
        time_delta = now - self.pub_date
        return time_delta.days == 0

    published_today.boolean = True
    published_today.short_description = "Published Today?"
