from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = "home"),
    path('post-login/', views.post_login_redirect, name='post_login_redirect'),
    path('accounts/logout/', allauth_views.logout, name='account_logout'),
    path("logout", views.logout_view),
    path('create/', views.student_create_view, name ="student_create"),
    path('list/', views.student_list_view, name ="profile"),
    path('create-campaign/', views.create_campaign, name="create_campaign"),
    path('create-campaign/load_more/', views.load_more_campaigns, name='load_more_campaigns'),
    path('update_campaign/<int:campaign_id>/', views.update_campaign, name="update_campaign"),
    path('delete_campaign/<int:campaign_id>/', views.delete_campaign, name="delete_campaign"),
    path('landing/', views.landing, name='landing'),
    path('rewards/', views.rewards_activity_view, name='rewards_activity'),
    path('rewards/redeem/<int:reward_id>/', views.redeem_reward, name='redeem_reward'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
