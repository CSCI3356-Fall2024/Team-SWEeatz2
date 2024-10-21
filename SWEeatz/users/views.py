from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def student_create_view(request):
    user = request.user
    student, created = Student.objects.get_or_create(user=user)  # Create or fetch the student's profile

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)  # Use the existing student instance
        if form.is_valid():
            form.save()  # Save updates
            return redirect('profile')  # Redirect to the profile page (adjust this as necessary)
    else:
        # Pre-populate the form with the user's data
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form, 'full_name': user.get_full_name()})
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'student_form.html', {'form':form})


def student_list_view(request):
    user = request.user
    student = get_object_or_404(Student, user=user)  # Fetch only the logged-in user's profile
    return render(request, 'student_list.html', {'student': student, 'full_name': user.get_full_name()})
    return render(request, 'student_list.html', {'students': students})