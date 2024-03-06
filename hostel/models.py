from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    # student_id = models.CharField(max_length=10,unique=True,null=True,blank=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    room_type = models.CharField(max_length=8)
    
    def __str__(self):
        return self.room_number

class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending')
    
    def __str__(self):
        return f"{self.title} by {self.student}"

class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null= True,blank=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
   
    def __str__(self):
        return f"Review for {self.student}"

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
   
    def __str__(self):
        return f"Fee for {self.student}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    present = models.BooleanField(default=False)
   
    def __str__(self):
        return f"Attendance for {self.student}"
