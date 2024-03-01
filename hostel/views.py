from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .decorators import cookie_required
from django.contrib.auth.hashers import check_password
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='/login/')
def profile(request):
    if 'username' in request.session:
        username = request.session['username']
        # Fetch the student based on the username
        student = Student.objects.get(username=username)
        
        # Fetch the attendance records of the student
        attendances = Attendance.objects.filter(student=student)
        fees = Fee.objects.filter(student=student)
        # Extract email and room from the student object
        email = student.email
        room = student.room
        
        context = {
            'student': student,
            'attendances': attendances,
            'fees':fees,
            'email': email,
            'room': room,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('/login/')

# @login_required(login_url='/login/')
def review(request):
    review = Review.objects.all()
    return render(request,'review.html',{'review':review})



def login_page(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists
        try:
            student = Student.objects.get(username=username)
        except Student.DoesNotExist:
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        # Check if the provided password matches the stored hashed password
        if not check_password(password, student.password):
            messages.error(request, "Invalid Password")
            return redirect('/login/')

        # Set user authentication
        request.session['username'] = username
        print(request.session.items())

        messages.success(request, "Login successful")
        return redirect('/profile/')

     return render(request, 'login.html')

def logout_page(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('/login/')

def Register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        existing_user = Student.objects.filter(username=username).first()

        if existing_user:
            messages.error(request, "Username already exists")
            return redirect('/register/')

        # Create a new Student instance
        new_student = Student(
            email=email,
            username=username,
        )
        new_student.set_password(password)  # Set the hashed password
        new_student.save()

        # Set user authentication
        request.session['username'] = username

        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, 'register.html')