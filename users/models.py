from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150,editable=False) # django 에 있는 필드를 사용하지 않음 - editable false
    last_name = models.CharField(max_length=150, editable=False)
    name=models.CharField(max_length=150,default="")
    is_host=models.BooleanField(default=False)