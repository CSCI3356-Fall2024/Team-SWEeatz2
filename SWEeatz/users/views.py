from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentForm
from .models import Student, Campaign
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "home.html")

def landing(request):
    return render(request, "landing.html")

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
        # Handle the form submission
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        image = request.FILES.get('image')
        points = request.POST.get('points', 0)

        if title and description and start_date and end_date:
            Campaign.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                image=image,
                points=points
            )
            return redirect('create_campaign')

    # Get the first 2 campaigns and the total count
    campaigns = Campaign.objects.all()[:2]
    total_campaigns = Campaign.objects.count()
    return render(request, 'campaign_create.html', {'campaigns': campaigns, 'total_campaigns': total_campaigns})

def load_more_campaigns(request):
    offset = int(request.GET.get('offset', 2))
    campaigns = Campaign.objects.all()[offset:]
    campaign_data = [
        {
            "id": campaign.id,
            "title": campaign.title,
            "description": campaign.description,
            "points": campaign.points,
            "start_date": campaign.start_date.strftime("%Y-%m-%d"),
            "end_date": campaign.end_date.strftime("%Y-%m-%d"),
            "image_url": campaign.image.url if campaign.image else None  # Handle missing image
        }
        for campaign in campaigns
    ]
    return JsonResponse({"campaigns": campaign_data})





@csrf_exempt
def update_campaign(request, campaign_id):
    if request.method == 'POST':
        try:
            campaign = Campaign.objects.get(id=campaign_id)
            
            # Retrieve updated fields
            title = request.POST.get('title', campaign.title)
            description = request.POST.get('description', campaign.description)
            start_date = request.POST.get('start_date', campaign.start_date)
            end_date = request.POST.get('end_date', campaign.end_date)
            points = request.POST.get('points', campaign.points)

            # Update text fields
            campaign.title = title
            campaign.description = description
            campaign.start_date = start_date
            campaign.end_date = end_date
            campaign.points = points

            # Handle image update or deletion
            if 'image' in request.FILES:
                campaign.image = request.FILES['image']  # Update with new image
            elif request.POST.get('delete_image') == 'true':
                campaign.image.delete(save=False)  # Delete existing image
                campaign.image = None

            campaign.save()

            # Return updated campaign data, including the image URL if it exists
            response_data = {
                "success": True,
                "image_url": campaign.image.url if campaign.image else None  # Updated image URL
            }
            return JsonResponse(response_data)
        except Campaign.DoesNotExist:
            return JsonResponse({"success": False, "error": "Campaign not found."})
    return JsonResponse({"success": False, "error": "Invalid request method."})


def delete_campaign(request, campaign_id):
    if request.method == 'POST':
        try:
            campaign = Campaign.objects.get(id=campaign_id)
            campaign.delete()
            return JsonResponse({"success": True})
        except Campaign.DoesNotExist:
            return JsonResponse({"success": False, "error": "Campaign not found."})







