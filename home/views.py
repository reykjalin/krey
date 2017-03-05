from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def loginView(request):
    if request.method == 'POST':
        print('post!')
        form = UserForm(request.POST)

        if form.is_valid():
            username = request.POST['user_name']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home/index.html')
        return render(request, 'home/login.html', { 'form': form })
    else:
        form = UserForm()
        return render(request, 'home/login.html', { 'form': form })

def logoutView(request):
    logout(request)
    return render(request, 'home/index.html')
