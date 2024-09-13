from django import forms
from django.contrib.auth.forms import UserCreationForm

from register.models import CustomUser


# Formulario de registro para Cliente
class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_nit = forms.CharField(max_length=20)
    company_name = forms.CharField(max_length=100)
    business_type = forms.CharField(max_length=100)
    country = forms.CharField(max_length=50)
    business_vertical = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    legal_representative = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        # Validar longitud y complejidad de la contraseña
        if len(password1) < 15:
            raise forms.ValidationError("The password must be at least 15 characters long.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("The password must contain at least one number.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("The password must contain at least one uppercase letter.")
        if not any(char in "!@#$%^&*()_+-=[]{}|;':,.<>?/`~" for char in password1):
            raise forms.ValidationError("The password must contain at least one special character.")

        return password2
