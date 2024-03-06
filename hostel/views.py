from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .decorators import cookie_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# from hostelmanagementsystem.hostel.forms import ReviewForm
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

# @login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def Add_review(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        # if not title or not content or not rating:
        #     # If any of the required fields are missing, return an error
        #     error_message = "Please fill out all the fields."
        #     return render(request, 'addreview.html', {'error_message': error_message}) 

        if 'username' in request.session:
            username = request.session['username']
            student = Student.objects.get(username=username)

            # Create a new review
            Review.objects.create(
                title=title,
                content=content,
                rating=rating,
                student_id=student.id
            )

            return redirect('review')  # Redirect to profile page
        else:
            return redirect('/addreview/')
        
    return render(request,'addreview.html')


def delete_review(request,review_id):
    if 'username' in request.session:
        username = request.session['username']
        student = Student.objects.get(username=username)

        review = Review.objects.get(pk=review_id)

        if review.student == student:
            review.delete()

    return redirect('review')  #


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

        # Set user authentication (You can use Django's built-in login method as well)
        request.session['username'] = username

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
        
        hashed_password = make_password(password)

        # Create a new Student instance
        new_student = Student(
            email=email,
            password=hashed_password,
            username=username,
        )
        
        new_student.save()

        # Set user authentication
        request.session['username'] = username

        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, 'register.html')