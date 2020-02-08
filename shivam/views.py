from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student


# Create your views here.

def hostel(request):
    studs = Student.objects.all()
    return render(request,'shivam.html',{'studs':studs})
def find(request):
    studs = Student.objects.all()
    name = (request.POST['name'])
    year = int(request.POST['year'])
    
    for stud in studs:
        x = stud.roomno
        y=stud.floorno
        if name == stud.name and year==stud.year:
            return render(request,'find.html',{'x':x,'y':y})
        


      
