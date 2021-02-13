from main_app.models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='REQUIRED, add a valid email',max_length=255)
    class Meta:
        model=Account
        fields=('email','username','password1','password2')
    
    def clean_email(self):
        email= self.cleaned_data['email']
        try:
            email=Account.objects.get(email=email)
        except :
            return email
        raise forms.ValidationError('The email has been registered')

        