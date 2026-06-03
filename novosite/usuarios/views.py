from urllib import request

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login_django(request, user)
            return HttpResponse('Login autenticado com sucesso.')
        else:
            return HttpResponse('e-mail ou senha inválidos.')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    
    username = request.POST.get('email')
    email = request.POST.get('email')
    password = request.POST.get('senha')
    first_name = request.POST.get('nome')

    user = User.objects.filter(username=username).first()

    if user:
        return HttpResponse('Usuário já existente!.')
    else:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name
        )
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!.')

def home(request):
    return render(request, 'usuarios/home.html')