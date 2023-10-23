from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",  # get 이 들어오면 list 함수 사용.
                "post": "create",
            }
        ),
    ),  # 클래스 불러오려면 as_view 붙여주어야 한다.
    path(
        "<int:pk>", # pk 로 작성해야retrieve 함수가 작동한다.
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",  # pk 가 필요하다.
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
