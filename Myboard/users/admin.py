from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# user과 profile이 한 모델인 것처럼 볼 수 있게 만듦
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)