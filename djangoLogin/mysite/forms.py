# models: premission, group, forms:
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class ChangePasswordUserForm(PasswordChangeForm):
    class Meta:
        model = User
        field = [
            'old_passowrd',
            'new_password1',
            'new_password2',
        ]