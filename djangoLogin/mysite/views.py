from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterUserForm


def index(request):
    context = {
        'title':'Beranda',
    }

    return render(request, 'index.html', context)


def register_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')

    if request.method == 'POST':
        register_user = RegisterUserForm(request.POST or None)
        if register_user.is_valid():
            messages.success(request, 'Berhasil Registrasi Akun')
            register_user.save()
            return redirect('login')
        else:
            messages.error(request, 'Gagal Registrasi Akun!')
    else:
        register_user = RegisterUserForm()

    context = {
        'title':'Register User',
        'form':register_user,

    }

    return render(request, 'register.html', context)


def login_user(request):
    context = {
        'title':'login',
    }

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')

    if request.method == 'POST':
        username_input = request.POST['username']
        password_input = request.POST['password']

        user = authenticate(request, username=username_input, password=password_input)

        if user is not None:
            login(request, user)
            messages.success(request, 'Anda Berhasil Login')
            return redirect('index')
        else:
            messages.error(request, 'Anda Gagal Login')
            return redirect('login')

    return render(request, 'login.html', context) 

@login_required(login_url='/')
def logout_user(request):
    context = {
        'title':'logout',
    }

    # if request.method == 'GET':
    #     if not request.user.is_authenticated:
    #         return redirect('index')

    if request.method == 'POST':
        if request.POST['logout'] == 'Logout':
            logout(request)
            messages.info(request, 'Anda Berhasil Logout')
            return redirect('index')
        else:
            messages.error(request, 'Anda Gagal Logout')
            return redirect('logout')

    return render(request, 'logout.html', context) 