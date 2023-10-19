from typing import Any
from django.db import models
from common.models import CommonModel  # 상속 받기 위해 커먼 모델을 생성해서 가져온다.


# Create your models here.
class Room(CommonModel):
    """_summary_
    room model definition
    """

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="south Korea")
    city = models.CharField(max_length=80, default="seoul")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",  # room_set 말고 rooms 로 가지게 된다.
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity", related_name="rooms",
    )  # 모델이 가지고 싶은 거
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        return self.amenities.count()
    
    def rating(self):
        count = self.reviews.count()
        if count==0:
            return "NO reviews"
        else:
            total_rating=0
            for review in self.reviews.all().values("rating"):
                total_rating+=review['rating']
            return round(total_rating/count,2)



# 장소가 제공해주는 옵션들. -> many to many relationship
class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150, null=True, blank=True
    )  # blank - django form, null - db

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
