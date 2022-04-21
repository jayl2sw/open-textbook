from django.db import models
from django.conf import settings
from datetime import datetime, timedelta, timezone

# Create your models here.
class Anonymous(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_anonymouses')
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    view_cnt = models.IntegerField(default=0)

    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return False


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anonymous = models.ForeignKey(Anonymous, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=50)


    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return False
    def __str__(self):
        return self.title