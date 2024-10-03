from django.shortcuts import render, redirect
from .models import LivingTime, Cabin, Visitor

# Create your views here.
def index(request):

    liv_time = LivingTime.objects.all()

    return render(request, "bookingapp/index.html", {'liv_time':liv_time})


def cabin_list(request):

    obj_list = Cabin.objects.all()

    return render(request, "bookingapp/cabin.html", {'cabin_list': obj_list})

def visitors_list(request):

    visit_list = Visitor.objects.all()

    return render(request, "bookingapp/visitors.html", {'visitors_list':visit_list})

def new_cabin(request):
    if request.method == 'POST':
        num=request.POST.get("cabin_num")
        type=request.POST.get("cabin_type")
        Cabin.objects.create(cabin_number=num, cabin_type=type)
        return redirect("cabin")


    return render(request, "bookingapp/new_cabin.html")


def reserve_cabin(request):
    if request.method == "POST":
        cabin_id = request.POST.get("residence_time")

        