from django.db import models
from common.models import CommonModel # 상속 받기 위해 커먼 모델을 생성해서 가져온다.

# Create your models here.
class Room(CommonModel):
	"""_summary_
		room model definition
	"""
	class RoomKindChoices(models.TextChoices):
		ENTIRE_PLACE=("entire_place","Entire place")
		PRIVATE_ROOM=("private_room","Private Room")
		SHARED_ROOM=("shared_room","Shared Room")


	country=models.CharField(max_length=50,default="south Korea")
	city=models.CharField(max_length=80,default="seoul")
	price=models.PositiveIntegerField()
	rooms=models.PositiveIntegerField()
	toilets=models.PositiveIntegerField()
	description=models.TextField()
	address=models.CharField(max_length=250)
	pet_friendly=models.BooleanField(default=True)
	kind=models.CharField(max_length=20,choices=RoomKindChoices.choices)
	owner=models.ForeignKey("users.User",on_delete=models.CASCADE,)
	amenities=models.ManyToManyField("rooms.Amenity")# 모델이 가지고 싶은 거






# 장소가 제공해주는 옵션들. -> many to many relationship
class Amenity(CommonModel):
	"""Amenity Definition"""
	name=models.CharField(max_length=150)
	description=models.CharField(max_length=150,null=True)
    