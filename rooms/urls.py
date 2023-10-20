from django.urls import path
from . import views


urlpatterns=[
    path("",views.see_all_rooms),
    path("<int:room_id>",views.see_one_rooms), # <타입 : 변수 이름. >
]