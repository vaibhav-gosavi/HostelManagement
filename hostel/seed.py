import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
import random
import string
from django.contrib.auth.hashers import make_password
from faker import Faker
from hostel.models import Student, Room, Complaint, Review, Fee, Attendance

fake = Faker()

# def generate_unique_student_id():
#     length = 8
#     while True:
#         student_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
#         if not Student.objects.filter(student_id=student_id).exists():
#             return student_id

def seed_students(number):
    for _ in range(number):
        # Generate fake data
        username = fake.user_name()
        email = fake.email()
        raw_password = 'password123'  # Change password if needed
        room = Room.objects.order_by('?').first()  # Randomly select a room

        # Hash the password
        hashed_password = make_password(raw_password)

        # Create a User
        user = User.objects.create_user(username=username, email=email, password=hashed_password)

        # Create a Student
        student = Student.objects.create(
            username=username,
            password=hashed_password,
            email=email,
            room=room
        )
        student.save()

def seed_rooms():
    room_types = ['Non-Ac', 'Ac']
    for i in range(1, 11):
        room = Room(
            room_number=f'Room-{i}',
            capacity=random.randint(1, 3),
            room_type=random.choice(room_types)
        )
        room.save()

def seed_complaints(number, students):
    for _ in range(number):
        complaint = Complaint(
            student=random.choice(students),
            title=fake.sentence(),
            description=fake.paragraph(),
            status=random.choice(['Pending', 'Resolved'])
        )
        complaint.save()

def seed_reviews(number, students):
    for _ in range(number):
        review = Review(
            student=random.choice(students),
            title=fake.sentence(),
            content=fake.paragraph(),
            rating=random.randint(1, 5)
        )
        review.save()

def seed_fees(number, students):
    for _ in range(number):
        fee = Fee(
            student=random.choice(students),
            amount=random.uniform(100, 1000),
            due_date=fake.date_this_year(),
            paid=random.choice([True, False])
        )
        fee.save()

def seed_attendance(number, students):
    for _ in range(number):
        attendance = Attendance(
            student=random.choice(students),
            date=fake.date_this_year(),
            present=random.choice([True, False])
        )
        attendance.save()

def seed_all():
    number_of_students = 20
    number_of_rooms = 10
    number_of_complaints = 30
    number_of_reviews = 30
    number_of_fees = 30
    number_of_attendance_records = 30

    seed_students(number_of_students)
    seed_rooms()
    
    students = list(Student.objects.all())

    seed_complaints(number_of_complaints, students)
    seed_reviews(number_of_reviews, students)
    seed_fees(number_of_fees, students)
    seed_attendance(number_of_attendance_records, students)

if __name__ == '__main__':
    seed_all()
    print("Database seeded successfully!")
