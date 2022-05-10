import imp
from mmap import PAGESIZE
from msilib.schema import File
from tkinter import Place
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from admin_challan.models import Challan, Signup

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.

def pdf(request):
    buf = io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup = 0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14) 

    # lines = [
    #     "this is line1",
    #     "this is line2",
    #     "this is line3",
    # ]

    challan_obj = Challan.objects.all()

    lines = []
    for challan in challan_obj:
        lines.append(challan.name)
        lines.append(challan.place)
        lines.append(str(challan.license))
        lines.append(str(challan.challan_num))
        lines.append(str(challan.traffic))
        lines.append(str(challan.fine))
        lines.append(challan.vehicle_type)
        lines.append(challan.created_by) 
        lines.append("")



    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="client.pdf")
     



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
            return render(request, "signin.html")


    return render(request, "signin.html")


def signup(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     password = request.POST.get("password")

    #     sign = Signup(
    #         name = name,
    #         email = email,
    #         password = password
    #     ) 

    #     sign.save()
    #     return redirect("signin")

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
        traffic = request.POST.get('traffic')
        fine = request.POST.get('fine')

        emp = Challan(
            name = name,
            place = place,
            license = license,
            challan_num = challan_num,
            traffic = traffic,
            fine = fine,
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
        traffic = request.POST.get('traffic')
        fine = request.POST.get('fine')

        emp = Challan(
            id = id,
            name = name,
            place = place,
            license = license,
            challan_num = challan_num,
            traffic = traffic,
            fine = fine,
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


def signin_traffic(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = name, password = password )

        if user is not None:
            login(request, user)
            return redirect("traffic_user")
        else:
            messages.success(request, ("There was an error Logging In, Try Again...."))
            return render(request, "signin_traffic.html")

    return render(request, "signin_traffic.html")


def traffic_user(request):
    emp = Challan.objects.all()

    context = {
        "emp" : emp, 
    }

    return render(request, "traffic_user.html", context)


def add_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        place = request.POST.get('place')
        license = request.POST.get('license')
        challan_num = request.POST.get('challan_num')
        vehicle_type = request.POST.get('vehicle_type')
        created_by = request.POST.get('created_by')
        traffic = request.POST.get('traffic')
        fine = request.POST.get('fine')

        emp = Challan(
            name = name,
            place = place,
            license = license,
            challan_num = challan_num,
            traffic = traffic,
            fine = fine,
            vehicle_type = vehicle_type,
            created_by = created_by
        )

        emp.save()
        return redirect("traffic_user")

    return render(request, "traffic_user.html")

def edit_user(request):
    emp = Challan.objects.all()

    context = {
        "emp" : emp,
    }
    return redirect(request, "traffic_user.html", context)

def update_user(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        place = request.POST.get('place')
        license = request.POST.get('license')
        challan_num = request.POST.get('challan_num')
        vehicle_type = request.POST.get('vehicle_type')
        created_by = request.POST.get('created_by')
        traffic = request.POST.get('traffic')
        fine = request.POST.get('fine')

        emp = Challan(
            id = id,
            name = name,
            place = place,
            license = license,
            challan_num = challan_num,
            traffic = traffic,
            fine = fine,
            vehicle_type = vehicle_type,
            created_by = created_by
        )

        emp.save()
        return redirect("traffic_user")

    return redirect(request, "traffic_user.html")


def traffic_rule(request):
    return render(request, "traffic_rule.html")



    

