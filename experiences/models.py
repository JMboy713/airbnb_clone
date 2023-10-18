from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    description = models.TextField()
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )
    category = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL,null=True,blank=True  # 카테고리가 삭제되더라도 삭제가 되지는 않는다.
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    """what is included on an Experience"""

    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
