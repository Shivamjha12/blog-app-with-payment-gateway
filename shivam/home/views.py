from django.shortcuts import render, HttpResponse
from home.models import profiledata


def homepage(request):
    return render(request, 'homepage.html')

def profile(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        ins = profiledata(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("Your data is saved in database")
    return render(request, 'profile.html')

def message(request):
    return render(request, 'message.html')

def android(request):
    return render(request, 'android_development.html')

def website(request):
    return render(request, 'website_development.html')

def videoediting(request):
    return render(request, 'video_animation.html')

def thankspage(request):
    return render(request, 'thanks.html')




# Create your views here.
