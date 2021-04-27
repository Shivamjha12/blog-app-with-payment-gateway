from django.contrib import admin
from django.urls import path
from home import views
 

admin.site.site_header = " Log In to Pritio Shivam Jha LTD Admin"
admin.site.siteheading = "Protio"
admin.site.site_title = "Pritio Shivam Jha LTD Admin panel"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('first', views.profile, name='profile'),
    path('message', views.message, name='msg'),
    path('android_development', views.android, name='android'),
    path('website_development', views.website, name='website'),
    path('video_animation', views.videoediting, name='videoediting'),
    path('usersignin', views.thankspage, name='Thankyou'),

    


]