# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TutorSignUpForm, StudentProfileForm, TutorProfileForm
from .models import User, Tutor, Hire

def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tutors = Tutor.objects.filter(subjects__icontains=search_query)
    else:
        tutors = Tutor.objects.all()
    return render(request, 'main/home.html', {'tutors': tutors})

def register_student(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = StudentSignUpForm()
    return render(request, 'registration/register_student.html', {'form': form})

def register_tutor(request):
    if request.method == 'POST':
        form = TutorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = TutorSignUpForm()
    return render(request, 'registration/register_tutor.html', {'form': form})

@login_required
def student_dashboard(request):
    student = request.user.student
    hires = Hire.objects.filter(student=student)
    return render(request, 'main/student_dashboard.html', {'student': student, 'hires': hires})

@login_required
def tutor_dashboard(request):
    tutor = request.user.tutor
    hires = Hire.objects.filter(tutor=tutor)
    return render(request, 'main/tutor_dashboard.html', {'tutor': tutor, 'hires': hires})

@login_required
def hire_tutor(request, tutor_id):
    student = request.user.student
    tutor = Tutor.objects.get(id=tutor_id)
    Hire.objects.create(student=student, tutor=tutor)
    messages.success(request, 'Tutor hired successfully.')
    return redirect('student_dashboard')

@login_required
def update_student_profile(request):
    student = request.user.student
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Failed to update profile. Please correct the errors below.')
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'main/update_student_profile.html', {'form': form})



@login_required
def update_tutor_profile(request):
    tutor = request.user.tutor
    if request.method == 'POST':
        form = TutorProfileForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('tutor_dashboard')
        else:
            messages.error(request, 'Failed to update profile. Please correct the errors below.')
    else:
        form = TutorProfileForm(instance=tutor)
    return render(request, 'main/update_tutor_profile.html', {'form': form})

