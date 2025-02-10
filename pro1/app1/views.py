from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer


# Create your views here.

def addview(request):
    form = CustomerForm()
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved!!!")
    return render(request,"form.html",{"form":form})


def sview(request):
    obj = Customer.objects.all()
    return render(request,"show.html",{"cust":obj})
