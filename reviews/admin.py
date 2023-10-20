from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ("good", "Good"),  # 첫번째 값은 url 에 표기될 글자.뒤에가 관리자 페이지에 나올 이름.
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request: Any, reviews) -> QuerySet[Any] | None:
        # reviews => 모든 리뷰들이 나온다.
        """
        print(reviews) # 필터링된 리뷰들만 나온다.
        print(request.GET) # GET 으로 가져온 Url 뒷부분을 받아올 수 있다.
        """
        # print(self.value())  # GET 으로 가져온 단어를 보여준다.
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)  # 쿼리셋.
        else:
            return reviews


class RatingFilter(admin.SimpleListFilter):
	title = "Filter by rating score by 3point"
	parameter_name = "score"

	def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
		return [
			("bad", "Bad"),
			("good", "Good"),
			
		]

	def queryset(self, request: Any, score) -> QuerySet[Any] | None:
		# print(self.value())
		rate=self.value()
		print(rate)
		if rate=="bad":
			return score.filter(rating__lt=3)
		else:
			return score.filter(rating__gte=3)




@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
        WordFilter,
        RatingFilter,
        # 필터는 순서대로 걸린다.
    )
