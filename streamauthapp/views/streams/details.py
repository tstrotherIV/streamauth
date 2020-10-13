import json
from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from streamauthapp.models import StreamEvent

@login_required(login_url='/login/stream')
def stream_details(request, event_id):
    if request.method == 'GET':
        stream = StreamEvent.objects.get(pk=event_id)
        print(stream.stream_embed)
        
        template = 'streamview/detail.html'
        context = {
            'stream': stream,
        }
        
        return render(request, template, context)


    
    
    