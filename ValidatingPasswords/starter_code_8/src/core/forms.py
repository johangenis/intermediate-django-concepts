from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django import forms

# settings.AUTH_USER_MODEL
User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError(
                    "The username or password was incorrect"
                )
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
