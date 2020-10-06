from django.urls import path
from django.conf.urls import include
from streamauthapp import views
from .views import *

app_name = "masterplanapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login, name='login'),
    path('register/', register_user, name="register"),
    path('accounts/logout/', logout_user, name='logout'),
    path('', home, name='home'),
]