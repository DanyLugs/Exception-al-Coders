from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, "login.html", context)

    def post(self, request):
        username = request.POST['username'],
        password = request.POST['password'],
        user = authenticate(request, username=username[0], password=password[0])

        if user is not None:
            print('Auth correct')
            login(request, user)
        else:
            print('Login Failed')
            print(username)
            print(password)

        form = AuthenticationForm(request.POST)
        context = {
            'form': form
        }
        return render(request, "login.html", context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class Signup(View):
    def get(self, request):
        context = {
            'form': SignUpForm()
        }
        return render(request, "signup.html", context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

        context = {
            'form': form
        }
        return render(request, "signup.html", context)
