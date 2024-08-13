from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from .filters import DetectionFilter
from .models import UploadAlert
from django.shortcuts import get_object_or_404

#testing
from django.core.mail import send_mail
from django.http import HttpResponse
import os

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'detection/login.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        #new add
        context={'form': form}

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for ' + user)
                return redirect('login')
            context={'form': form}
        return render(request, 'detection/register.html', context)

@login_required(login_url='login')
def home(request):
    token = Token.objects.get(user=request.user)
    uploadAlert = UploadAlert.objects.filter(user_ID = token).order_by('-date_created')
    myFilter = DetectionFilter(request.GET, queryset=uploadAlert)
    uploadAlert = myFilter.qs
    context = {'myFilter': myFilter, 'uploadAlert': uploadAlert}

    return render(request, 'detection/dashboard.html', context)

def logoutUser (request):
    logout(request)
    return redirect('login')
'''
def alert(request, pk):
    #uploadAlert = UploadAlert.objects.filter(image = str(pk) + ".jpg")
    uploadAlert = UploadAlert.objects.filter(pk=pk)
    myFilter = DetectionFilter(request.GET, queryset=uploadAlert)
    uploadAlert = myFilter.qs
    context = {'myFilter':myFilter, 'uploadAlert': uploadAlert}

    return render(request, 'detection/alert.html', context)
'''

def alert(request, pk):
    #uploadAlert = UploadAlert.objects.filter(pk=pk)    
    #myFilter = DetectionFilter(request.GET, queryset=uploadAlert)
    #uploadAlert = myFilter.qs
    #context = {'UploadAlert': uploadAlert}#, 'myFilter':myFilter}

    #specific_alert = get_object_or_404(UploadAlert, pk=pk)
    #all_alerts = UploadAlert.objects.all()
    #myFilter = DetectionFilter(request.GET, queryset=all_alerts)
    #filtered_alerts=myFilter.qs

    #context={
        #'UploadAlert': specific_alert,
        #'myFilter': myFilter,
        #'filtered_alerts': filtered_alerts
    #}

    uploadAlert = UploadAlert.objects.filter(pk=pk)
    myFilter = DetectionFilter(request.GET, queryset=uploadAlert)
    filtered_alert = myFilter.qs

    context = {
        'myFilter': myFilter,
        'alert': filtered_alert.first(),  # Get the first (and should be only) item
        'uploadAlert': filtered_alert
    }

    return render(request, 'detection/alert.html', context)

