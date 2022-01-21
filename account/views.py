from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})
