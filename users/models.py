from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices): # 고르게 하는거
        MALE=("male","Male") #  value 가 들어갈 튜플. db에 저장될 값, 관리자가 볼 label
        FEMALE=("female","Female")
    class LanguageChoices(models.TextChoices):
        KR=("kr","Korean") # db에 저장될 거는 maxlength 보다 작아야 한다. 
        EN=("en",'English')
    class CurrencyChoices(models.TextChoices):
        WON=("won","Korean Won")
        USD=('usd',"Dollar")

    first_name = models.CharField(max_length=150,editable=False) # django 에 있는 필드를 사용하지 않음 - editable false
    last_name = models.CharField(max_length=150, editable=False)
    avatar=models.ImageField(blank=True) # pillow 를 설치해야 사용할 수 있다. , blank=true -> 빈칸도 비어둘 수 있게 해주는것. 
    name=models.CharField(max_length=150,default="")
    is_host=models.BooleanField(default=False)
    gender=models.CharField(max_length=10,choices=GenderChoices.choices)
    language=models.CharField(max_length=2,choices=LanguageChoices.choices)
    currency=models.CharField(max_length=5,choices=CurrencyChoices.choices)