from django.db import models
from django.conf import settings
# Create your models here.
class Algorithm(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_algorithms')
    title = models.CharField(max_length=20)
    site_url = models.CharField(max_length=50)
    content = models.TextField()
    input = models.TextField()
    output = models.TextField()
    constricts = models.TextField()
    examples = models.TextField()
    level = models.CharField(max_length=3)



class Solution(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_solutions')
    hint = models.TextField()
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    description = models.TextField()
    solution_code = models.TextField()



class Solution_Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)