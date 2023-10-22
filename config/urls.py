from django.contrib import admin
from django.urls import path,include
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', include("rooms.urls")), # 처음에 갈 곳, 실행할 함수.
    path('categories/',include("categories.urls")),
]
