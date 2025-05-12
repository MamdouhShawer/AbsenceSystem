from django.shortcuts import render, redirect
from .forms import AbsenceFormForm
from .models import Student, AbsenceForm

def submit_absence(request):
    student = Student.objects.first()  # Replace with actual login logic later

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
