from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = "Your password should contain at least 8 characters."
        self.fields['password2'].help_text = "Enter the same password as before, for verification."

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter a username....'})
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter a password....'})
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password....'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
       