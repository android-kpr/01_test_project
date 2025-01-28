from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    account_id = models.IntegerField()
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

