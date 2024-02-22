import random
from faker import Faker
from django.utils import timezone
from hostel.models import Student, Room, Complaint, Review, Fee, Attendance, Event

fake = Faker()

# Seed function to populate models with fake data
def seed_data():
    
    for _ in range(50):
        student = Student.objects.create(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
            student_id=fake.unique.random_number(digits=6)
        )

    
    rooms = []
    for _ in range(10):
        rooms.append(Room.objects.create(
            room_number=fake.unique.random_number(digits=3),
            capacity=random.randint(1, 4)
        ))

    
    for _ in range(20):
        student = random.choice(Student.objects.all())
        Complaint.objects.create(
            student=student,
            title=fake.sentence(),
            description=fake.paragraph(),
            status=random.choice(['Pending', 'Resolved'])
        )

    
    for _ in range(20):
        student = random.choice(Student.objects.all())
        Review.objects.create(
            student=student,
            title=fake.sentence(),
            content=fake.paragraph(),
            rating=random.randint(1, 5)
        )

    
    for _ in range(20):
        student = random.choice(Student.objects.all())
        Fee.objects.create(
            student=student,
            amount=random.uniform(100, 1000),
            due_date=fake.date_this_year(),
            paid=random.choice([True, False])
        )

   
    for _ in range(20):
        student = random.choice(Student.objects.all())
        Attendance.objects.create(
            student=student,
            date=fake.date_this_year(),
            present=random.choice([True, False])
        )

    for _ in range(10):
        organizer = random.choice(Student.objects.all())
        attendees = random.sample(list(Student.objects.all()), random.randint(1, 20))
        event = Event.objects.create(
            title=fake.sentence(),
            description=fake.paragraph(),
            date=fake.date_this_year(),
            time=fake.time(),
            location=fake.address(),
            organizer=organizer
        )
        event.attendees.add(*attendees)

if __name__ == '__main__':
    seed_data()
