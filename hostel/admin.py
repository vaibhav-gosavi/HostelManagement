from django.contrib import admin
from . models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email' , 'room')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Room)
admin.site.register(Complaint)
admin.site.register(Review)
admin.site.register(Fee)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'present']

admin.site.register(Attendance, AttendanceAdmin)