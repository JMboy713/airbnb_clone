from django.shortcuts import render
from django.http import HttpResponse
from .models import Room



'''
def say_hello(request): # request object 로 받는게 무엇인지 판단한다. 
    return HttpResponse("say_hello")
'''

def see_all_rooms(request):
    rooms=Room.objects.all()
    return render(request,"all_rooms.html",{'rooms':rooms,'title':"Hello this title is from django"}) # 보내줄 데이터 

def see_one_rooms(request,room_id):
    return HttpResponse(f"room number is {room_id}")
