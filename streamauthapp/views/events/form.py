from django.shortcuts import render, redirect

def event_form(request):
    if request.method == 'GET':
        template = 'events/eventInfo.html'
        

        return render(request, template)