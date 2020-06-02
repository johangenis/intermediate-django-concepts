from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms

# settings.AUTH_USER_MODEL
User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password'
        ]