from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request):
    return render(request,'room.html')

def complaint(request):
    return render(request,'complaint.html')

def review(request):
    return render(request,'review.html')

def fee(request):
    return render(request,'fee.html')

def attendance(request):
    return render(request,'attendance.html')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        existing_user = Student.objects.filter(username=username).exists()

        if not existing_user:
            messages.success(request, "Invalid Username") 
            return redirect('/login/')

        user = authenticate(username = username , password = password)
        if user is None:
             messages.error(request, "Invalid Password") 
             return redirect('/login/') 

        else:
            login(request,user)
            return redirect('/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def Register_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username is provided in the POST request
        if not username:
            # Handle the case where username is not provided (you can redirect or show an error message)
            return render(request, 'register.html', {'error_message': 'Username is required'})

        # Check if the username already exists
        existing_user = Student.objects.filter(username=username).first()
        
        if existing_user:
            messages.error(request, "Username already exists") 
            return redirect('/register/')

        # Create a new user
        # user = Student.objects.create(
        #     email = email
        #     username=username
        # )
        # user.set_password(password)
        # user.save()

        messages.success(request, "Account created successfully")
        return redirect('/register/')

    return render(request, 'register.html')



