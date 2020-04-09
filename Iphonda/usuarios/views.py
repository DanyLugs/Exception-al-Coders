from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
# Create your views here.
class Login(View):
    def get(self, request):
        context = {}
        return render(request, "login.html", context)


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
