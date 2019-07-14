from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from . models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email')

class CustomUSerChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields