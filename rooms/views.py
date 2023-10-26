from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from categories.models import Category
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly # GET은 통과, post 는 인증받는사람만 간으하게 해준다. 

"""
/api/v1/rooms/amenities/
/api/v1/rooms/amenities/1
"""


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()  # 유효하다면 저장하고 보여준다.
            return Response(
                AmenitySerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        # amenity=self.get_object(pk)
        # serializer=AmenitySerializer(amenity)
        return Response(
            AmenitySerializer(self.get_object(pk)).data,
        )

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        # print(request.user) authenticated 된 유저라면 정보를 받아올 수 있다.
        
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required.")  # 잘못된 데이터 형식을 가지고 있을 때.
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("the category should be rooms")
                except Category.DoesNotExist:
                    raise ParseError("category not found")

                try:
                    with transaction.atomic():  # db에 바로 반영하지 않고, 변경 사항들을 리스트로 만들어서 다 저장되면 DB 로 Push
                        room = serializer.save(
                            owner=request.user,
                            category=category,
                        )  # create 메서드에 **validated_data 에 추가된다.
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity not found")
            else:
                return Response(serializer.errors)
        
        


class RoomDetail(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)
        
        
        if room.owner != request.user:
            raise PermissionDenied
        else:
            serializer = RoomDetailSerializer(room, data=request.data, partial=True)
            if serializer.is_valid():
                updated_room = serializer.save()
                return Response(RoomDetailSerializer(updated_room).data)
            else:
                return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        
        
        if room.owner != request.user:
            raise PermissionDenied
        else:
            room.delete()
            return Response(status=HTTP_204_NO_CONTENT)


class RoomReviews(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            # print(request.query_params) # 쿼리의 파라미터를 읽어온다.
            page = request.query_params.get("page", 1)  # 없으면 기본값 1.
            page = int(page)  # str 로 가져온다. 또한 정수만 받는다.
        except ValueError:
            page = 1
        page_size = 3
        start = (page - 1) * page_size
        end = start + page_size

        room = self.get_object(pk)
        serializer = ReviewSerializer(
            room.reviews.all()[start:end],  # 쿼리 셋이기 때문에 먼저 가져오게 한다.
            many=True,
        )
        return Response(serializer.data)


class RoomAmenities(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            # print(request.query_params) # 쿼리의 파라미터를 읽어온다.
            page = request.query_params.get("page", 1)  # 없으면 기본값 1.
            page = int(page)  # str 로 가져온다. 또한 정수만 받는다.
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        room = self.get_object(pk)
        serializer = AmenitySerializer(
            room.amenities.all()[start:end],  # 쿼리 셋이기 때문에 먼저 가져오게 한다.
            many=True,
        )
        return Response(serializer.data)


class RoomPhotos(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        
        room = self.get_object(pk)
        if request.user != room.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(room=room)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
