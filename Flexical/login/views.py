from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
    form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})
