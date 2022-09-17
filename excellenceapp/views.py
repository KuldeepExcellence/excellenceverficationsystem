
from django.shortcuts import render,HttpResponse,redirect
from .models import verification
from django.contrib import messages

# Create your views here.


def home(request):
    return render (request,"verify.html")


def verify(request):
    if request.method=="POST":
        enrollment_no = request.POST.get("enrollment_no")
        data = verification.objects.filter(enrollment_no=enrollment_no).values()
        if data.exists():
            context={
                'data':data
                }
            return render(request,'index.html',context)
        else:
            messages.error(request,"Record Not Found")
            return redirect ("home")
    
    return render(request,'index.html')



  