from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #pra login
from django.contrib.auth import authenticate, login, logout #pra poder autenticar
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')  # Corrigi para 'cars_list' que é o name da sua URL
        # Remove o else aqui - mantemos o formulário com erros
    else:
        user_form = UserCreationForm()  # Formulário vazio para GET
  
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)  # Use o formulário para validação
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cars_list')
        # Se não for válido, o formulário já contém os erros
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('cars_list')
