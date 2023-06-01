from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        user_name = request.POST['first_name']
        password = request.POST['password'] 

        user = authenticate(request,username = user_name , password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            print("Error")
            messages.error(request,"First Name or Password is Wrong!")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    print("Logout Clicked")
    logout(request)
    messages.success(request,"You have been successfully Logged Out...")
    return redirect('home')

def register_user(req):
    return render(req,'register.html',{})