from django.shortcuts import render

# Create your views here.


def HomePage(request):
    pass

def SignupPage(request):
    return render (request, 'signup.html')

def LoginPage(request):
    pass
