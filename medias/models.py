from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
	file = models.ImageField()
	description = models.CharField(
		max_length=140,
	)
	room = models.ForeignKey(
		"rooms.Room",
		on_delete=models.CASCADE,
		null=True,
		blank=True,
	)
	experience = models.ForeignKey(
		"experiences.Experience",
		on_delete=models.CASCADE,
		null=True,
		blank=True,
	)
	def __str__(self) -> str:
		return "Photo File"


class Video(CommonModel):
	file = models.FileField()
	experience = models.OneToOneField(
		"experiences.Experience",
		on_delete=models.CASCADE,
	)  # 활동은 오직 1개의 동영상만 있다.  FK 와 같지만 고유한 값이 된다. 동영상이 하나의 활동과 연결되면 다른 동영상은 가질 수 없다.
	def __str__(self) -> str:
		return "Video file"

# onetoone field : 결제정보 데이터에 사요할 수 있다.
