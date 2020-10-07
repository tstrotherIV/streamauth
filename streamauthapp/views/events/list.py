from django.shortcuts import render, redirect
from django.urls import reverse
from streamauthapp.models import StreamEvent

def event_list(request):
    if request.method == "GET":
      event_list = StreamEvent.objects.all()
      template_name = 'events/list.html'
      
      context = {
        'all_events': event_list
      }
      
      return render(request, template_name, context)
  
    elif request.method == 'POST':
        form_data = request.POST
        
        StreamEvent.objects.create(
            name = form_data['name'],
            description = form_data['description'],
            stream_embed = form_data['stream_embed'],
            chat_feed = form_data['chat_feed'],
          )


        return redirect(reverse('streamauthapp:events'))