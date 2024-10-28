from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentForm
from .models import Student, Campaign
from django.shortcuts import get_object_or_404
from django.utils import timezone
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

def post_login_redirect(request):
    user = request.user

    # Check if the user already has a Student profile
    try:
        student = Student.objects.get(user=user)
        # If the user has a profile, redirect them to the list page
        return redirect('profile')  # or whatever URL name you have for the list page
    except Student.DoesNotExist:
        # If no profile exists, redirect them to the profile creation page
        return redirect('student_create')

def student_list_view(request):
    user = request.user
    student = get_object_or_404(Student, user=user)  # Fetch only the logged-in user's profile
    if user.is_superuser:
        role = "Admin"
    else:
        role = "Student"
    return render(request, 'student_list.html', {'student': student, 'full_name': user.get_full_name(), 'role':role})

def create_campaign(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Validate and save the data
        if title and description and start_date and end_date:
            # Create a new Campaign instance
            Campaign.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date
            )
            return redirect('create_campaign')  # Redirect to the same page after saving

    # If GET request, display the form and existing campaigns
    campaigns = Campaign.objects.all()  # Retrieve all existing campaigns
    return render(request, 'campaign_create.html', {'campaigns': campaigns})