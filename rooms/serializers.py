from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers
from reviews.serializers import ReviewSerializer
from wishlists.models import Wishlist


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
        )
        # depth = 1  # id 를 보고 해당 데이터를 가져옴, 커스터마이즈할 수 없다.

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return (
            room.owner == request.user
        )  # request 한 사람과 소유자가 같은지 확인. 소유자 여부에 따라 수정 버튼을 보이게, 안보이게 할 수 있따.


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )  # common 은 read_only 로 읽힌다.


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(
        read_only=True
    )  # request에서 요구하지 않는다.  # user 에서 설정한 serializer 쓰라고 설정.  owner 쓸때 Tiny serializer을 사용.
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):  # 메서드 이름은 속성의 이름 앞에 get_ 을 붙여야 한다.
        # print(room) # room 의 이름이 따라온다.
        # print(self.context) # serializer 에 담겨오는 데이터.
        return room.rating()  # 함수 호출.

    def get_is_owner(self, room):
        request = self.context["request"]
        return (
            room.owner == request.user
        )  # request 한 사람과 소유자가 같은지 확인. 소유자 여부에 따라 수정 버튼을 보이게, 안보이게 할 수 있따.

    def get_is_liked(self, room):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user=request.user, rooms__pk=room.pk
        ).exists()  # 유저가 여러개의 위시리스트를 가지고 있을 수 있으니 filter 사용.
