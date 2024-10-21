from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
urlpatterns = [
    path('', views.home, name = "home"),
    path('post-login/', views.post_login_redirect, name='post_login_redirect'),
    path('accounts/logout/', allauth_views.logout, name='account_logout'),
    path("logout", views.logout_view),
    path('create/', views.student_create_view, name ="student_create"),
    path('list/', views.student_list_view, name ="profile"),
]