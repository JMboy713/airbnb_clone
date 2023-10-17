from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets=(
        (
            "Profile",
            {"fields":("username","password","name","email",'is_host','avatar','gender','currency','language',),
                    "classes":("wider"),
                    },
                    
                    ),
        (
            "permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes":("collapse",)
            },
        ),
        (
         "Important dates",{"fields": ("last_login", "date_joined")}
         ),
    )
    #fields=("email","password","name") # fieldset 을 맘대로 저장. 
    list_display=("username","email",'name','is_host')
    # 여기에 나오는 필드명들은 models.py 에 꼭 있어야 한다.!!!!