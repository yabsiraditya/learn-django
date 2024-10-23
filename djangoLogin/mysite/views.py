from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    context = {
        'title':'Beranda',
    }

    return render(request, 'index.html', context)


def login_user(request):
    context = {
        'title':'login',
    }

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


def logout_user(request):
    context = {
        'title':'logout',
    }

    if request.method == 'POST':
        if request.POST['logout'] == 'Logout':
            logout(request)
            messages.info(request, 'Anda Berhasil Logout')
            return redirect('index')
        else:
            messages.error(request, 'Anda Gagal Logout')
            return redirect('logout')

    return render(request, 'logout.html', context) 