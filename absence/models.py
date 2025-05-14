from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ✅ This is required
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.student_id} - {self.name}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ✅ link to Django's User
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class AbsenceForm(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    teacher_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Form by {self.student.name} - {self.status}"


class AbsenceReview(models.Model):
    form = models.OneToOneField(AbsenceForm, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    reviewed_at = models.DateTimeField(auto_now=True)
    decision = models.CharField(max_length=10, choices=[('approved', 'Approved'), ('rejected', 'Rejected')])
    feedback = models.TextField()

    def __str__(self):
        return f"{self.form.student.name} - {self.decision}"


class Notification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.student.name} on {self.date_sent.strftime('%Y-%m-%d')}"


