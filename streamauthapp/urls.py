from django.urls import path
from django.conf.urls import include
from streamauthapp import views
from .views import *

app_name = "streamauthapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login, name='login'),
    path('register/', register_user, name="register"),
    path('accounts/logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('events/', event_list, name='events'),
    path('events/form/', event_form, name='event_form'),
    path('events/<int:event_id>/', event_details, name='event'),
    path('form/<int:event_id>', event_details, name='event_details'),
    path('stream/<int:event_id>/', stream_details, name='stream'),
]