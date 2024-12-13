from django import forms
from django .forms import ModelForm


from .models import Venue



#create a venue form

class VenueForm(forms.ModelForm):
    class Meta:
       model = Venue
       fields = ['name', 'address', 'zip_code', 'phone' , 'web','email_address']

       labels = {
           'name': '',
           'address':'',
           'zip_code':'',
           'phone':'',
           'web':'',
           'email_address':''
       }

       widgets = {
           'name': forms.TextInput(attrs={'class':"form-control",'style':'width:20%',}),
           'address': forms.TextInput(attrs={'class':'form-control','style':'width:50%',}),
           'zip_code': forms.TextInput(attrs={'class':'form-control','style':'height:100px'}),
           'phone': forms.TextInput(attrs={'class':'form-control','style':'width:50%',}),
           'web': forms.TextInput(attrs={'class':'form-control','style':'width:50%',}),
           'email_address': forms.EmailInput(attrs={'class':'form-control','style':'width:50%',}),

       }







