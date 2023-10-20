from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="set all prices to zero")
def reset_prices(model_admin,request,rooms): # request : 누가 호출했는지 확인. 
    print(request)
    for room in rooms.all(): #query set 이기 때문에 가능.
        room.price=0
        room.save()
    




@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions=(reset_prices,)


    list_display = (
        "name",
        "price",
        "rating",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "amenities",
    )
    search_fields = (
        "^name",  # startswith 를 뜻함.
        "price",
    )

    def total_amenities(self, room):
        return room.amenities.count()

    search_fields = (
        "owner__username", # FK 로 검색한다. 
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at",)
