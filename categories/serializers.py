from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 카테고리를 위한 시리얼라이저를 만듬.
        fields = "__all__"
        
        # exclude=() 제외할 것으로 설정할 것이라면 exclude 사용. 
		# fields="__all__" -> 모두를 사용할 것이다. 
