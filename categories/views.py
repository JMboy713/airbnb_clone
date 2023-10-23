from .models import Category
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .serializers import CategorySerializer


"""
Get/Response
Get/Response/1
"""


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":  # db -> 시리얼라이저.
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    # return JsonResponse({'ok':True,'cate':all_catetories}) -> 쿼리셋은 json으로 바로 못준다.. json 포맷으로 바꿔주어어야 한다.
    # rest_framework => 번역기 serializer 필요.
    elif request.method == "POST":  # user -> Serializer
        serializer = CategorySerializer(data=request.data)  # data= xxx...
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT"])
def category(request, pk):
	try:
		category = Category.objects.get(pk=pk)
	except Category.DoesNotExist:
		raise NotFound
	if request.method == "GET":
		serializer = CategorySerializer(category)
		return Response(serializer.data)
	elif request.method == "PUT":
		serializer = CategorySerializer(
			category,
			data=request.data,
			partial=True, # 부분에 대해서만 수정이 가능하게 해준다. request받지 못한 데이터는 원본을 그대로 사용한다. 
		)

		if serializer.is_valid():
			updated_category=serializer.save()
			return Response(CategorySerializer(updated_category).data)
			# serializer.save() # put 에서 save 를 호출하면 Serializer의 update를 호출한다. 
		else:
			return Response(serializer.errors)


# Post 요청
