from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """wish list model definitions"""

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        "rooms.Room",
        related_name='wishlist',
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='wishlists',
    )
    def __str__(self) -> str:
        return self.name