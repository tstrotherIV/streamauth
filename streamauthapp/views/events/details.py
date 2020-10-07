import json
from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from streamauthapp.models import StreamEvent


@login_required
def event_details(request, event_id):
    if request.method == 'GET':
        event = StreamEvent.objects.get(pk=event_id)
        
        template = 'events/detail.html'
        context = {
            'event': event,
        }
        
        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            event_to_update = StreamEvent.objects.get(pk=event_id)
            

            event_to_update.name = form_data['name']
            event_to_update.description = form_data['description']
            event_to_update.stream_embed = form_data['stream_embed']
            event_to_update.chat_feed = form_data['chat_feed']
            
            event_to_update.save()
            
            return redirect(reverse('streamauthapp:events'))
        

    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "ARCHIVE"
            ):

                event_to_archive = StreamEvent.objects.get(pk=event_id)
                event_to_archive.deleted = True
                
                event_to_archive.save()


                return redirect(reverse('streamauthapp:events'))
            
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "RESTORE"
            ):

                event_to_restore = StreamEvent.objects.get(pk=event_id)
                event_to_restore.deleted = False
                
                event_to_restore.save()


                return redirect(reverse('streamauthapp:eventsArchives'))
            
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "NUKE"
            ):

                event_to_delete = StreamEvent.objects.get(pk=event_id)
                event_to_delete.delete()


                return redirect(reverse('streamauthapp:projects'))
    
    