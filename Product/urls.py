from django.urls import path
from .views import *
from .import views



urlpatterns = [
    path('',  Home,name='Home'),
    path('athletics/',Atheletics,name= 'Athletics'),
    path('about/',About, name='About'),
    path('calendar/',Calendar,name='Calendar'),
    path('chamb/',Chamb,name='Chamb'),
    path('course/',Course,name='Course'),
    path('media/',Media,name='Media'),
    path('mission/',Mission,name=' Mission'),
    path('enroll/',Enroll,name='Enroll'),
    path('schedules/',DailySchedules,name='DailySchedules'),
    path('register/',Register,name='Register'),
    path('dining/',Dining,name='Dining'),
    path('family/',Family,name='Family'),
    path('post/',Post,name=' Post'),
    path('gov/',Gov,name='Gov'),
    path('service/',Service,name='Service'),
    path('statement/',State,name='State'),
    path('rules/',Rules,name='Rules'),
    path('more/',More,name='More'),
    path('read/',Read,name='Read'),
    path('employment/',Employment,name='Employment'),
    path('dona/',Dona,name='Dona'),
    path('confidential/', Confidential, name='Confidential'),
    path('advocate/', Advacate, name='Advocate'),
    path('cross/', Cross, name='Cross'),
    path('add_venue',views.add_venue ,name='add-venue'),
    path('ball/', Ball, name='ball'),
    path('volley/', Volley, name='Volley'),

    path('sports/<int:sports_id>',Sports ,name='sports'),



]