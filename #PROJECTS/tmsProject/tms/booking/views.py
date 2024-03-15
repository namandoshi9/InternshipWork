from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .form import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'index.html')

def tripDetails(request):
    return render(request, 'trip&packgeDetails.html')


def abouUs(request):
    return render(request,'about.html')


def ServiceView(request):
    return render(request,'service.html')


def ContectUs(request):
    return render(request,'contact.html')


def Packges_view(request):
    packages = Package.objects.all()
    return render(request,'package.html',{'packages':packages})


def destination_view(request):
    destinations = Destination.objects.all()
    return render(request,'destination.html',{'destinations': destinations})



@login_required
def booking_detail_view(request):
    # Fetch bookings for the logged-in user
    user_profile = request.user.userprofile
    bookings = Booking.objects.filter(user_profile=user_profile)
    return render(request, 'booking.html', {'bookings': bookings})























def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


@csrf_protect
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            response = redirect('index')
            response.set_cookie('username', user.username)
            return response
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def user_logout(request):
    logout(request)
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    response = redirect('index')
    response.delete_cookie('username')
    return response

