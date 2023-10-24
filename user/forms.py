from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {'first_name': "Ism",
                  'last_name': "Familiya",
                  'username': "Foydalanuvchi nomi"}
