from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings
from .models import Farmer, GovernmentAgency, NGO, Contact
from django.http import JsonResponse
import numpy as np
import pickle
import os
from django.contrib.auth.decorators import login_required




# Load models and scalers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))
sc = pickle.load(open(os.path.join(BASE_DIR, 'minmaxscaler.pkl'), 'rb'))
mx = pickle.load(open(os.path.join(BASE_DIR, 'standscaler.pkl'), 'rb'))




# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must log in to access this page.")
        return redirect("login")

    # Fetch user information if needed
    user_id = request.session['user_id']
    username = request.session['username']
    user_type = request.session['user_type']

    context = {
        "username": username,
        "user_type": user_type,
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        contacts=Contact.objects.all()
        mycontact = Contact(
            name = request.POST["name"],
            email = request.POST["email"],
            subject = request.POST["subject"],
            message = request.POST["message"],
        )
        mycontact.save()
        return render(request, "contactinfo.html", {"contact": contacts})
    else:
        return render(request,"contact.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blog.html")

def testimonials(request):
    return render(request, "testimonials.html")

def blogdetails(request):
    return render(request, "blog-details.html")

def contactinfo(request):
    return render(request, "contactinfo.html")

def delete(request,id):
    deleted = Contact.objects.get(id=id)
    deleted.delete()
    return redirect("/contactinfo")

# Farmer Registration View
def farmer_register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        location = request.POST['location']
        soil_type = request.POST.get('soil_type', '')  # Optional field
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        # Check if passwords match before hashing
        if password != confirmpassword:
            messages.error(request, "Passwords do not match. Please try again.", extra_tags="danger")
            return redirect('farmer_register')

        # Check if the email is already registered
        if Farmer.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.", extra_tags="danger")
            return redirect('farmer_register')

        # Hash the password and create the Farmer record
        hashed_password = make_password(password)
        Farmer.objects.create(
            full_name=full_name,
            email=email,
            location=location,
            soil_type=soil_type,
            password=hashed_password
        )
        messages.success(request, "Registration successful! Please log in.", extra_tags="success")
        return redirect('login')

    return render(request, 'farmerregister.html')

# Government Agency Registration View
def gov_register(request):
    if request.method == 'POST':
        agency_name = request.POST['agency_name']
        contact_person = request.POST['contact_person']
        email = request.POST['email']
        region = request.POST['region']
        password = request.POST['password']  # Get plain password from form
        confirmpassword = request.POST['confirmpassword']  # Get confirm password from form

        # Check if passwords match before hashing
        if password != confirmpassword:
            messages.error(request, "Passwords do not match. Please try again.", extra_tags="danger")
            return redirect('gov_register')

        # Check if email already exists
        if GovernmentAgency.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.", extra_tags="danger")
            return redirect('gov_register')

        # Hash the password
        hashed_password = make_password(password)

        # Create the Government Agency record
        GovernmentAgency.objects.create(
            agency_name=agency_name,
            contact_person=contact_person,
            email=email,
            region=region,
            password=hashed_password
        )

        messages.success(request, "Registration successful! Please log in.", extra_tags="success")
        return redirect('login')

    return render(request, 'govregister.html')


# NGO Registration View
def ngo_register(request):
    if request.method == 'POST':
        organization_name = request.POST['organization_name']
        email = request.POST['email']
        focus_area = request.POST.get('focus_area', '')  # Optional field
        password = request.POST['password']  # Get plain password from form
        confirmpassword = request.POST['confirmpassword']  # Get confirm password from form

        # Check if passwords match before hashing
        if password != confirmpassword:
            messages.error(request, "Passwords do not match. Please try again.", extra_tags="danger")
            return redirect('ngo_register')

        # Check if email already exists
        if NGO.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.", extra_tags="danger")
            return redirect('ngo_register')

        # Hash the password
        hashed_password = make_password(password)

        # Create the NGO record
        NGO.objects.create(
            organization_name=organization_name,
            email=email,
            focus_area=focus_area,
            password=hashed_password
        )

        messages.success(request, "Registration successful! Please log in.", extra_tags="success")
        return redirect('login')

    return render(request, 'ngoregister.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check for Farmer
        user = Farmer.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['user_type'] = 'farmer'
            messages.success(request, f"Welcome, {user.full_name}!")
            return redirect('home')

        # Check for Government Agency
        user = GovernmentAgency.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['user_type'] = 'government_agency'
            messages.success(request, f"Welcome, {user.agency_name}!")
            return redirect('home')

        # Check for NGO
        user = NGO.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['user_type'] = 'ngo'
            messages.success(request, f"Welcome, {user.organization_name}!")
            return redirect('home')

        messages.error(request, "Invalid email or password!", extra_tags="danger")
        return redirect('login')

    return render(request, 'login.html')

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#
#         # Check for Farmer
#         user = Farmer.objects.filter(email=email).first()
#         if user and check_password(password, user.password):
#             request.session['user_id'] = user.id
#             request.session['user_name'] = user.full_name
#             request.session['user_email'] = user.email
#             request.session['user_location'] = user.location
#             messages.success(request, f"Welcome, {user.full_name}!")
#             next_url = request.GET.get('next', 'dashboard')  # Default to 'dashboard' if no next URL
#             return redirect(next_url)
#
#         # Check for Government Agency
#         user = GovernmentAgency.objects.filter(email=email).first()
#         if user and check_password(password, user.password):
#             request.session['user_id'] = user.id
#             request.session['user_name'] = user.agency_name
#             request.session['user_email'] = user.email
#             request.session['user_location'] = user.location
#             messages.success(request, f"Welcome, {user.agency_name}!")
#             next_url = request.GET.get('next', 'dashboard')
#             return redirect(next_url)
#
#         # Check for NGO
#         user = NGO.objects.filter(email=email).first()
#         if user and check_password(password, user.password):
#             request.session['user_id'] = user.id
#             request.session['user_name'] = user.organization_name
#             request.session['user_email'] = user.email
#             request.session['user_location'] = user.location
#             messages.success(request, f"Welcome, {user.organization_name}!")
#             next_url = request.GET.get('next', 'dashboard')
#             return redirect(next_url)
#
#         messages.error(request, "Invalid email or password.")
#         return redirect('login')
#
#     return render(request, 'login.html')
#
# @login_required
# def dashboard_view(request):
#     # Retrieve user details from the session
#     user_name = request.session.get('user_name')
#     user_email = request.session.get('user_email')
#     user_location = request.session.get('user_location')
#
#     # Pass user details to the template
#     return render(request, 'dashboard.html', {
#         'user_name': user_name,
#         'user_email': user_email,
#         'user_location': user_location
#     })
def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('login')


def landing(request):
    return render(request, "landing.html")


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if the email exists in any of the tables (User, NGO, GovernmentAgency)
        user_exists = Farmer.objects.filter(email=email).exists()
        ngo_exists = NGO.objects.filter(email=email).exists()  # Replace with actual NGO email field
        gov_exists = GovernmentAgency.objects.filter(email=email).exists()  # Replace with actual field

        if user_exists or ngo_exists or gov_exists:
            # Logic to send password reset email (use Django's built-in mechanism)
            # send_password_reset_email(email)  # Custom method to send an email

            # For simplicity, let's send a mock email.
            send_mail(
                'Password Reset Request',
                'Click the link below to reset your password.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, "A password reset email has been sent.")
            return redirect('login')  # Redirect user to login page
        else:
            messages.error(request, "Email not found in our records.")
            return render(request, 'forgotpassword.html')

    return render(request, 'forgotpassword.html')

def recommend(request):
    if request.method == 'POST':
        try:
            # Get form inputs
            N = float(request.POST['Nitrogen'])
            P = float(request.POST['Phosporus'])
            K = float(request.POST['Potassium'])
            temp = float(request.POST['Temperature'])
            humidity = float(request.POST['Humidity'])
            ph = float(request.POST['pH'])
            rainfall = float(request.POST['Rainfall'])

            # Prepare input features
            feature_list = [N, P, K, temp, humidity, ph, rainfall]
            single_pred = np.array(feature_list).reshape(1, -1)

            # Apply scaling transformations in the correct order
            mx_features = mx.transform(single_pred)  # Standard scaling
            sc_mx_features = sc.transform(mx_features)  # Min-max scaling

            # Predict using the model
            prediction = model.predict(sc_mx_features)

            # Get the predicted crop
            crop = prediction[0]  # Assuming the model outputs the crop name directly
            result = f"{crop} is the best crop to be cultivated right there."

        except Exception as e:
            result = f"An error occurred during prediction: {e}"

        # Return the recommendation with the result
        return render(request, 'recommend.html', {'result': result})

    return render(request, 'recommend.html')

def dashboard(request):
    return render(request, "dashboard.html")