from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def register_user(request):
    """Handles creation of a new user for auth
        Args:
        request = full http object
    """

    # For handling when user submits the form data
    if request.method == "POST":

        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )
    

        authenticated_user = authenticate(
            username=request.POST['username'], password=request.POST['password'])

        if authenticated_user is not None:
            login(request, authenticated_user)

            # Redirect the browser to wherever you want to go after registering
            return redirect(reverse('masterplanapp:home'))

    # handles a request to load the empty form for the user to fill out
    else:
        template = 'registration/registration.html'

    return render(request, template, {})
