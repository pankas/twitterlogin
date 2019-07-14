from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCreationForm,CustomUSerChangeForm
from . models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUSerChangeForm

admin.site.register(CustomUser,CustomUserAdmin)
