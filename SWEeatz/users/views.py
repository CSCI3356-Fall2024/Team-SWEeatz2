from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentForm
from .models import Student
# Create your views here.

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def student_create_view(request):
    form = StudentForm()
    #if request.method == 'POST':
     #   form = StudentForm(request.POST)
     #   if form.is_valid():
    #        form.save()
   #         return redirect('profile')
    #return render(request, 'student_form.html', {'form':form})
    user = request.user
    # Try to get the existing Student instance for the logged-in user
    student, created = Student.objects.get_or_create(user=user)  # Creates a new instance if none exists

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)  # Use the existing student instance
        if form.is_valid():
            form.save()  # Save updates to the existing student
            return redirect('profile')  # Redirect after successful save
    return render(request, 'student_form.html', {'form':form})


def student_list_view(request):
    students = Student.objects.all()
    logged_in_student = Student.objects.get(user=request.user)
    return render(request, 'student_list.html', {'students': students,'logged_in_student':logged_in_student})