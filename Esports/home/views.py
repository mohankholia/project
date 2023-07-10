from django.shortcuts import render, HttpResponse
from home.models import Signup
from django.contrib import messages
# Create your views here.


def home(request):
    # return HttpResponse("Hello")
    return render(request, "Home.html")


def about(request):
    return render(request, "About.html")


def ranking(request):
    return render(request, "Ranking.html")


def contest(request):
    return render(request, "Contest.html")


def login(request):
    messages.success(request, "Welocme Back!!")
    return render(request, "Login.html")


def signup(request):
    messages.success(request, "Welocme User!!")
    return render(request, "Signup.html")


def profile(request):
    return render(request, "Profile.html")


def submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if (name[0].isdigit()):
            messages.error(request, "Please Enter A Valid Name")
            return render(request, "Signup.html")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if (len(password) < 4):
            messages.error(request, "Password length should be 4 or greater")
            return render(request, "Signup.html")
        phone = request.POST.get("phone")
        if (len(phone) != 10):
            messages.error(request, "Please Enter a Vlaid Phone Number")
            return render(request, "Signup.html")
        for i in range(0, len(Signup.objects.all())):
            if Signup.objects.all()[i].email == email:
                messages.error(request, "User Already Exists. Please Login!!")
                return render(request, "Signup.html")

            sign = Signup(name=name, email=email,
                          mobile=phone, password=password)
            sign.save()
        context = {
            "name": name,
            "email": email,
            "phone": phone
        }
        return render(request, "Profile.html", context)


def welcome(request):
    if (request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        for i in range(0, len(Signup.objects.all())):
            if (Signup.objects.all()[i].email == email and Signup.objects.all()[i].password == password):
                context = {
                    "name": Signup.objects.all()[i].name,
                    "email": Signup.objects.all()[i].email,
                    "phone": Signup.objects.all()[i].mobile,
                }
                return render(request, "Profile.html", context)
        messages.error(request, "Wrong Details!!")
        return render(request, "Login.html")
