from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from apps.users.forms import LoginForm, UserRegistrationForm


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.User, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully registered")
            return redirect('goodread:login-page')
        else:
            return render(request, "register.html", {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.User)
        if form.is_valid():
            user = authenticate(request, username=request.User.get("username"), password=request.User.get("password"))
            if user is not None:
                login(request, user)
                messages.success(request, "User successfully logged in")
                return redirect("goodread:home")
            else:
                messages.warning(request, "User not found")
                return redirect("goodread:login-page")
        else:
            return render(request, "login.html", {"form": form})
