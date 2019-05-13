from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    pass
    # username = models.CharField(max_length=50)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.username
    #     # return self.user.username
