from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
	"""Booking Model Definition"""

	class BookingKindChoices(models.TextChoices):
		ROOM = ("room", "Room")
		EXPERIENCE = "experience", "Experience"

	kind = models.CharField(
		max_length=15,
		choices=BookingKindChoices.choices,
	)
	user = models.ForeignKey(
		"users.User",
		on_delete=models.CASCADE,
	)
	room = models.ForeignKey(
		"rooms.Room",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)  # 룸이 삭제되어도 기록에는 있어야 한다.
	experience = models.ForeignKey(
		"experiences.Experience",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)
	# room을 위한 체크인, 체크아웃
	checkin = models.DateField(
		null=True,
		blank=True,
	)
	checkout = models.DateField(
		null=True,
		blank=True,
	)  # 안쓸때도 있기 때문에.
	# 경험을 위한 시간. 
	experience_time = models.DateTimeField(
		null=True,
		blank=True,
	)
	guests=models.PositiveIntegerField()

	def __str__(self) -> str:
		if self.kind =="room":
			return f"{self.user} : {self.room}"
		else:
			return f"{self.user} : {self.experience}"
