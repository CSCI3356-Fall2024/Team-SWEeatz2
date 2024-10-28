from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentForm
from .models import Student, Campaign
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test

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

# Custom function to check if user is an admin
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url='home')  # Redirects non-admins to home
def create_campaign(request):
    if request.method == 'POST':
        # Handle the campaign creation form submission
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        image = request.FILES.get('image')
        
        if title and description and start_date and end_date:
            Campaign.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                image=image
            )
            return redirect('create_campaign')

    # Show only the first 2 campaigns initially
    campaigns = Campaign.objects.all()[:2]
    return render(request, 'campaign_create.html', {'campaigns': campaigns})

def load_more_campaigns(request):
    """Handles loading additional campaigns via AJAX."""
    offset = int(request.GET.get('offset', 2))
    limit = 2  # Number of additional campaigns to load each time
    campaigns = Campaign.objects.all()[offset:offset + limit]
    
    # Prepare data for JSON response
    campaign_data = [
        {
            "title": campaign.title,
            "description": campaign.description,
            "start_date": campaign.start_date.strftime("%Y-%m-%d"),
            "end_date": campaign.end_date.strftime("%Y-%m-%d"),
            "image_url": campaign.image.url if campaign.image else None
        }
        for campaign in campaigns
    ]
    return JsonResponse({"campaigns": campaign_data})

