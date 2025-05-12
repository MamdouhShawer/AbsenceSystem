from django.contrib import admin
from .models import Student, Teacher, AbsenceForm, AbsenceReview, Notification

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(AbsenceForm)
admin.site.register(AbsenceReview)
admin.site.register(Notification)

admin.site.site_header = "University Absence System Admin"