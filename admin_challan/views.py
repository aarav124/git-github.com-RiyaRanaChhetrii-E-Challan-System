from tkinter import Place
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from admin_challan.models import Challan

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = name, password = password )

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.success(request, ("There was an error Logging In, Try Again...."))
            return redirect('signin')


    return render(request, "signin.html")


def signup(request):
    return render(request, "signup.html")


def dashboard(request):
    emp = Challan.objects.all()

    context = {
        "emp" : emp, 
    }

    return render(request, "dashboard.html", context)

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        place = request.POST.get('place')
        license = request.POST.get('license')
        challan_num = request.POST.get('challan_num')
        vehicle_type = request.POST.get('vehicle_type')
        created_by = request.POST.get('created_by')

        emp = Challan(
            name = name,
            place = place,
            license = license,
            challan_num = challan_num,
            vehicle_type = vehicle_type,
            created_by = created_by
        )

        emp.save()
        return redirect("dashboard")

    return render(request, "dashboard.html")

def edit(request):
    emp = Challan.objects.all()

    context = {
        "emp" : emp,
    }
    return redirect(request, "dashboard.html", context)

def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        place = request.POST.get('place')
        license = request.POST.get('license')
        challan_num = request.POST.get('challan_num')
        vehicle_type = request.POST.get('vehicle_type')
        created_by = request.POST.get('created_by')

        emp = Challan(
            id = id,
            name = name,
            place = place,
            license = license,
            challan_num = challan_num,
            vehicle_type = vehicle_type,
            created_by = created_by
        )

        emp.save()
        return redirect("dashboard")

    return redirect(request, "dashboard.html")


def delete(request, id):
    emp = Challan.objects.filter(id = id)
    context = {
        "emp" : emp,
    }
    emp.delete()

    return redirect("dashboard")


