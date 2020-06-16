from django.shortcuts import render
from django.views import View

# Create your views here.
class HomePage(View):
    def get(self, request):
        grupo = str(request.user.groups.all().first());
        return render(request, 'home.html', {
            'title': 'Bienvenido',
            'grupo': grupo
        })
