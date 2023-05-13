from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Add error message for invalid credentials
            context = {'error_message': 'Invalid username or password.'}
            return render(request, 'login.html', context=context)
    else:
        return render(request, 'login.html')
    
def dashboard(request):
    return render(request, "dashboard.html")