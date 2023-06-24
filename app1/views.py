from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email=request.POST.get('email')
        pas1=request.POST.get('password1')
        pas2=request.POST.get('password2')
        my_user=User.objects.create_user(username,email,pas1)
        my_user.save()
        return HttpResponse("Akun berhasil dibuat")
        print(username,email,pas1,pas2)

    return render(request, 'signup.html')

def LoginPage(request):
    return render(request, 'login.html')

