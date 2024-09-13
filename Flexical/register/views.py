from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from register.forms import ClientRegistrationForm
from register.models import ClientProfile


# Create your views here.
def register (response):
    if response.method == 'POST':
        registrationForm = UserCreationForm(response.POST)
        if registrationForm.is_valid():
            registrationForm.save()    
    else:
        registrationForm = UserCreationForm()

    return render(response, 'register/register.html', {'form':registrationForm})


def registerPFrelancer(request):
    return render(request, 'register/registerPFrelancer.html')


# Vista para registro de Cliente
def register_client(request):
    if request.method == 'POST':
        user_form = ClientRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'client'  # Asignamos el tipo de usuario
            user.save()
            ClientProfile.objects.create(
                user=user,
                company_nit=user_form.cleaned_data.get('company_nit'),
                company_name=user_form.cleaned_data.get('company_name'),
                business_type=user_form.cleaned_data.get('business_type'),
                country=user_form.cleaned_data.get('country'),
                business_vertical=user_form.cleaned_data.get('business_vertical'),
                city=user_form.cleaned_data.get('city'),
                address=user_form.cleaned_data.get('address'),
                phone_number=user_form.cleaned_data.get('phone_number'),
                legal_representative=user_form.cleaned_data.get('legal_representative')
            )
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio
        else:
            print(user_form.errors)
    else:
        user_form = ClientRegistrationForm()

    return render(request, 'register/register_client.html', {'user_form': user_form})