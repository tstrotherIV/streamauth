from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'GET':
        template = 'viewer_login.html'
        context = {}

        return render(request, template, context)
