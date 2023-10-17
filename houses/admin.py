from django.contrib import admin
from .models import House

@admin.register(House) # admin이 관리하게 될 모델은 House라고 등록. 
class HouseAdmin(admin.ModelAdmin): # model 관리자를 상속
	list_display = ["name","price_per_night","description","address","pets_allowed"] # 위에 이름 붙이기.
	list_filter=["price_per_night","pets_allowed"]# 필터 만들어주기. 
	
