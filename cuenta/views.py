""" from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden.')
            else:
                user.set_password(password1)
                user.save()
                # autenticar al usuario y redirigir al dashboard
                user = authenticate(request, username=user.username, password=password1)
                if user is not None:
                    login(request, user)
                    messages.success(request, '¡Bienvenido! Tu cuenta ha sido creada exitosamente.')
                    return redirect('registro_exitoso')
    else:
        form = RegisterForm()
    return render(request, 'cuenta/registro.html', {'form': form})

def registro_existoso(request):
    return render(request,'cuenta/registro_exitoso.html') """