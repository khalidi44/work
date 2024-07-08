from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def HomePage(request):
    return render(request, 'shop/home.html')


def shopPage(request):
    return render(request, 'shop/shopPage.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def searchMatch():
    pass
def search(request):
    return render(request, 'shop/search.html')
def productView(request):
    return render(request, 'shop/productView.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return redirect("error")
        elif len(uname) == 0:
            return redirect("error2")
        elif len(email) == 0:
            return redirect("error2")
        elif len(pass1) == 0:
            return redirect("error2")
        elif len(pass2) == 0:
            return redirect("error2")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'shop/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('ShopHome')
        else:
            return redirect('error')
    return render(request, 'shop/login.html')


def error(request):
    return render(request, 'shop/password_incorrect.html')

def error2(request):
    return render(request, 'shop/password_incorrect2.html')

def LogoUt(request):
    return render(request,'shop/logoutPage.html')

def Logout(request):
    logout(request)
    return redirect('homePAGE')