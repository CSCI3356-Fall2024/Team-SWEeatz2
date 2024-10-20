from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path("logout", views.logout_view),
    path('create/', views.student_create_view, name ="student_create"),
    path('list/', views.student_list_view, name ="profile"),
]