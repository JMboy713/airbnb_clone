from django.shortcuts import render
from .models import Category
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def categories(request):
    all_categories=Category.objects.all()
    return Response({'ok':True,})
	# return JsonResponse({'ok':True,'cate':all_catetories}) -> 쿼리셋은 json으로 바로 못준다.. json 포맷으로 바꿔주어어야 한다.
