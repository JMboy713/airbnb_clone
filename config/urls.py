from django.contrib import admin
from django.urls import path,include
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/rooms/', include("rooms.urls")), # 처음에 갈 곳, 실행할 함수.
    path('apu/v1/categories/',include("categories.urls")),
]
