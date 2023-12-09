from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class Create(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'birth_year']

class Change(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'birth_year']
        
