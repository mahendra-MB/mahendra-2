from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # ✅ Import User model

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        else:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()  # ✅ Ensure the user is saved

            messages.success(request, "Registration successful! Please login.")
            return redirect("login")

    return render(request, "registration.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("destinations")  # ✅ Redirect to destinations page after login
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')

@login_required
def destinations_view(request):
    print("✅ destinations_view is being called!")

    holiday_trips = [
        {"country": "France", "city": "Paris", "description": "Visit the Eiffel Tower and Louvre Museum."},
        {"country": "Italy", "city": "Rome", "description": "Explore the Colosseum and Vatican City."},
        {"country": "Japan", "city": "Tokyo", "description": "Experience traditional and modern culture in Tokyo."},
        {"country": "USA", "city": "New York", "description": "See Times Square, Statue of Liberty, and Broadway."},
        {"country": "UAE", "city": "Dubai", "description": "Enjoy the luxury and skyscrapers of Dubai."}
    ]

    print("✅ Holiday Trips Data Sent to Template:", holiday_trips)  # Debugging print

    return render(request, "destinations.html", {"user": request.user, "tours": holiday_trips})  # Pass correct variable


from django.contrib.auth import logout  # ✅ Import logout

def logout_view(request):
    logout(request)
    return redirect("home")  # Redirect user to home page after logout
