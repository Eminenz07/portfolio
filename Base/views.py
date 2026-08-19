from django.shortcuts import render, redirect
from django.contrib import messages
from Base import models

def home(request):
    return render(request, "home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = (request.POST.get("message") or request.POST.get("content") or "").strip()

        if len(name) < 2 or len(name) > 40:
            messages.error(
                request,
                "Length of name should be between 2 and 40 characters.",
            )
            return render(request, "home.html")

        if len(email) < 3 or len(email) > 50:
            messages.error(request, "Please provide a valid email address.")
            return render(request, "home.html")

        if not message:
            messages.error(request, "Please enter your message before submitting.")
            return render(request, "home.html")

        if phone and (len(phone) < 7 or len(phone) > 15):
            messages.error(request, "Invalid phone number, please try again.")
            return render(request, "home.html")

        ins = models.Contact(name=name, email=email, message=message, phone=phone)
        ins.save()

        messages.success(
            request, "Thank you for reaching out! Your message has been sent successfully."
        )

    return render(request, "home.html")
