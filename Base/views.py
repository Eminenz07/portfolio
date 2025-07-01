from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact


# from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, "home.html")


# @login_required(login_url='')
def contact(request):
    if request.method == "POST":
        print("post")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, email, phone, message)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(
                request,
                "Length of name should be greater than 2 and less than 30 characters",
            )
            return render(request, "home.html")

        if len(email) > 1 and len(email) < 30:
            pass
        else:
            messages.error(request, "invalid email try again")
            return render(request, "home.html")

        if phone and len(phone) > 9 and len(phone) < 13:
            pass
        else:
            messages.error(request, "invalid phone please try again")
            return render(request, "home.html")

        ins = models.Contact(name=name, email=email, message=message, phone=phone)
        ins.save()

        messages.success(
            request, "Thank You for contacting me!! Your message has been saved"
        )
        print("data has been saved to database")

        print("The request is no pass ")
    return render(request, "home.html")
