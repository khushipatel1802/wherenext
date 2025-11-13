

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages


users_data = [] 

packages = [
    {"id":1, "name":"Goa Beach Trip", "price":6999, "duration":"3N/4D", "desc":"Relaxing beach stay."},
    {"id":2, "name":"Himachal Hills", "price":9999, "duration":"4N/5D", "desc":"Mountains and trekking."},
    {"id":3, "name":"Rajasthan Tour", "price":14999, "duration":"5N/6D", "desc":"Palaces & desert safari."},
]

def home(request):
    username = request.session.get("username")
    return render(request, "wherenext_a/home.html", {"packages": packages, "username": username})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        mobile = request.POST.get("mobile", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not (username and email and mobile and password and password2):
            messages.error(request, "All fields required.")
            return redirect("wherenext_a:signup")
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("wherenext_a:signup")

       
        for u in users_data:
            if u["username"].lower() == username.lower():
                messages.error(request, "Username already taken.")
                return redirect("wherenext_a:signup")
            if u["mobile"] == mobile:
                messages.error(request, "Mobile already registered.")
                return redirect("wherenext_a:signup")

        users_data.append({
            "username": username,
            "email": email,
            "mobile": mobile,
            "password": password
        })
        messages.success(request, "Signup successful. Please login.")
        return redirect("wherenext_a:login")

    return render(request, "wherenext_a/signup.html")

def login(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier", "").strip() 
        password = request.POST.get("password", "")
        if not (identifier and password):
            messages.error(request, "Please enter credentials.")
            return redirect("wherenext_a:login")

        user = None
        for u in users_data:
            if u["username"].lower() == identifier.lower() or u["mobile"] == identifier:
                user = u
                break

        if user and user["password"] == password:
            request.session["username"] = user["username"]
            messages.success(request, f"Welcome, {user['username']}!")
            return redirect("wherenext_a:home")

        messages.error(request, "Invalid credentials.")
        return redirect("wherenext_a:login")

    return render(request, "wherenext_a/login.html")

