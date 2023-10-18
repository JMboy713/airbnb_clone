from django.db import models
from common.models import CommonModel


# 방 -> 방에 유저가 여러명 있을 수 있다.
#
class ChattingRoom(CommonModel):
    """room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
    )
    def __str__(self) -> str:
        return "chatting room"


class Message(CommonModel):
    """message moduls definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )
    def __str__(self) -> str:
        return f"{self.user} : {self.text}"
