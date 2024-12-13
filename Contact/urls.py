from tkinter.font import names

from django.urls import path

from Contact.views import Contact

urlpatterns = [
    path('contact/',Contact,name='contact' ),


]
