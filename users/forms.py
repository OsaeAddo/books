from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreatioForm(UserCreationForm):
    class meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

