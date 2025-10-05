from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SigupPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
        else:
            return HttpResponse("password not meached ! ")

    return render(request,'singup.html')

def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("incurrect password or username !")

    return render(request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')