from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

#Signup route/setting
def SignupPage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email=request.POST.get('email')
        pas1=request.POST.get('password1')
        pas2=request.POST.get('password2')

        if pas1!=pas2:
            return HttpResponse("password tidak sesuai")
        else:

            my_user=User.objects.create_user(username,email,pas1)
            my_user.save()
            return redirect("login")
            print(username,email,pas1,pas2)

    return render(request, 'signup.html')


#login setting setup
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username,password=pass1)
        if user is not None:
            return redirect('home')
        else:
            return HttpResponse ('Username dan Password tidak sesuai')
    return render(request, 'login.html')


def LogoutPage(request):
        logout(request)
        return redirect('login')