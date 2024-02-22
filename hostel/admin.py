from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Complaint)
admin.site.register(Review)
admin.site.register(Fee)
admin.site.register(Attendance)
