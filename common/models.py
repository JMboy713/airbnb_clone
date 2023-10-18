from django.db import models

# db 에 넣지 않을 모델, 다른 모델에서 사용하기 위한 모델일 뿐. 
class CommonModel(models.Model):
	"""Common Model Definition"""
	created_at=models.DateField(auto_now_add=True) # 필드값을 object 가 처음 생성되었을때 시간을 넣는다.
	updated_at=models.DateField(auto_now=True) # 필드값을 object 가 저장될 때의 시간을 넣는다.

	# db에 저장하지 않기 위한 코드
	class Meta: # model 을 configure 할 때 사용. 
		abstract=True #db 에 추가하지 않는 코드

