from django.urls import path
from apps.settings.views import nok
 
urlpatterns = [
    path('',nok,name='nok')
]