from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from .forms import CreateUserForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Profile was successfully created')
            return redirect('accounts:login')

    return render(request, 'accounts/signup.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('articles:index')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('articles:index')
        else:
            raise ValidationError("Username or password is incorrect!")
    return render(request, 'accounts/login.html')
