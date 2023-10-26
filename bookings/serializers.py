from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CretaeRoomBookingSerializEr(serializers.ModelField):
	checkin=serializers.DateField()
	checkout=serializers.DateField()

	class Meta:
		model=Booking
		field=("checkin","checkout","guest",)
	def validate_checkin(self,value): # is_valid 를 실행할 수 있게해준다. 
		now=timezone.localtime(timezone.now()).date()
		if now>value:
			raise serializers.ValidationError("cant book")
		return value
	
	def validate_checkout(self,value): # is_valid 를 실행할 수 있게해준다. 
		now=timezone.localtime(timezone.now()).date()
		if now<value:
			raise serializers.ValidationError("cant book")
		return value
        
class PublicBookingSerializer(serializers.ModelSerializer): # 퍼블릭.
    class Meta:
        model = Booking
        fields = (
            "pk",
            "checkin",
            "checkout",
            "experience_time",
            "guests",
        )
