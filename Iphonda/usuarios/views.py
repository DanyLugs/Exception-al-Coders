from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Login(View):
    def get(self, request):
        context = {}
        return render(request, "login.html", context)


class Signup(View):
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, "signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            form.clean()

        context = {
            'form': form
        }
        return render(request, "signup.html", context)
