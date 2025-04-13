from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,'profiles/home.html')

from django.contrib import messages
def addprofile(request):
    if request.method == 'POST':
        form = infoform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Submitted Successfully')
            # return render(request,'profiles/profile.html',{'form':form,'show':show})
            return redirect('profile')
        else:
            show = 'Invalid Data'
            return render(request,'profiles/profile.html',{'form':form,'show':show})
    else:
        form = infoform()
        return render(request,'profiles/profile.html',{'form':form})

def viewprofiles(request):
    view = info.objects.all()
    return render (request,'profiles/profileslist.html',{'view':view})

def searchprofiles(request):
    if request.method == "POST":
        form = searchform(request.POST)
        if form.is_valid():
            date = form.cleaned_data['select']
            pro = info.objects.filter(date = date)
            return render (request,'profiles/searchit.html',{'pro':pro})
        else:
            return render(request,'profiles/searchit.html',{'error':'Invalid input'})
    else:
        form = searchform()
        return render (request,'profiles/search.html',{'form':form})
    
def searchit(request,date):
    pro = info.objects.filter(submit=date)
    return render (request,'profiles/searchit.html',{'pro':pro})
