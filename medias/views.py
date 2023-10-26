from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import Photo
from rest_framework.exceptions import NotFound, PermissionDenied


class PhotoDetail(APIView):
	# property 추가. (인증을 위한. )
	permission_classes=[IsAuthenticated]

	def get_object(self, pk):
		try:
			return Photo.objects.get(pk=pk)
		except Photo.DoesNotExist:
			raise NotFound

	def delete(self, request, pk):
		photo = self.get_object(pk)
		if (photo.room and photo.room.owner != request.user) or (
			photo.experience and photo.experience.host != request.user
		):  # 방이 있다면,
			raise PermissionDenied
		photo.delete()
		return 
		