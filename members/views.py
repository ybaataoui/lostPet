from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST": # check if the user sent the request or just visiting
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_pets')
        else:
            messages.success(request, 'There was an Error logon in try again ...!')
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Were Logged Out!')
    return redirect('home')