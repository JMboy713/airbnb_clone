from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    def update(self, instance, validated_data):	# instance : DB에서 받아온 데이터, validated_data : request	 에서 받아온 데이터
        instance.name=validated_data.get("name",instance.name) # get으로 찾고 있다면 그대로 가고 없다면 바꾼다. 
        instance.kind=validated_data.get("kind",instance.kind)            
        instance.save()
        return instance
                       
