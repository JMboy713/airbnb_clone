from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )
        # depth = 1  # id 를 보고 해당 데이터를 가져옴, 커스터마이즈할 수 없다.


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )  # common 은 read_only 로 읽힌다.


class RoomDetailSerializer(ModelSerializer):
    owner = (
        TinyUserSerializer()
    )  # user 에서 설정한 serializer 쓰라고 설정.  owner 쓸때 Tiny serializer을 사용.
    amenities = AmenitySerializer(many=True)
    category=CategorySerializer()
    class Meta:
        model = Room
        fields = "__all__"
