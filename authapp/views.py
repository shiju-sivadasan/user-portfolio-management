from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def user_register(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('user_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('user_register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request, 'User Registered')
                return redirect('user_login')
    return render(request, 'accounts/register.html')

def user_login(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'User Logged In')
            return redirect('create_portfolio')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('user_login')
    return render(request, 'accounts/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('user_login')