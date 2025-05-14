from django.shortcuts import render, redirect
from .forms import AbsenceFormForm
from .models import Student, AbsenceForm
from .models import AbsenceForm, AbsenceReview, Teacher
from .forms import AbsenceReviewForm
from django.contrib.auth import login
from .forms import StudentSignupForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_absence(request):
    student = request.user.student

    if request.method == 'POST':
        form = AbsenceFormForm(request.POST)
        if form.is_valid():
            absence = form.save(commit=False)
            absence.student = student
            absence.save()
            return render(request, 'absence/submitted.html')
    else:
        form = AbsenceFormForm()

    return render(request, 'absence/submit.html', {'form': form})

def review_list(request):
    pending_forms = AbsenceForm.objects.filter(status='pending')
    return render(request, 'absence/review_list.html', {'forms': pending_forms})


def review_form(request, form_id):
    absence_form = AbsenceForm.objects.get(id=form_id)

    if request.method == 'POST':
        form = AbsenceReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.form = absence_form
            review.teacher = Teacher.objects.first()  # Temporary test teacher
            review.save()

            # Update the AbsenceForm
            absence_form.status = review.decision
            absence_form.teacher_feedback = review.feedback
            absence_form.save()

            return redirect('review_list')
    else:
        form = AbsenceReviewForm()

    return render(request, 'absence/review_form.html', {
        'absence_form': absence_form,
        'form': form
    })

@login_required
def my_absences(request):
    student = request.user.student
    forms = AbsenceForm.objects.filter(student=student).order_by('-submitted_at')
    return render(request, 'absence/my_absences.html', {'forms': forms, 'student': student})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(
                user=user,
                student_id=form.cleaned_data['student_id'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            login(request, user)
            return redirect('my_absences')
    else:
        form = StudentSignupForm()
    return render(request, 'absence/signup.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'student'):
            return redirect('my_absences')
        elif hasattr(request.user, 'teacher'):
            return redirect('review_list')
    return render(request, 'absence/home.html')
