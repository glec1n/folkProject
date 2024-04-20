from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']
        labels = {
            "username": "Логин"
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль'})        
        self.fields['password2'].widget.attrs.update({'placeholder': 'Подтверждение пароля'})