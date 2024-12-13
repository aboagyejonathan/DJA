from django.db.models import Q
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
class Away:
    pass

def Contact(request):
    if request.method=="post":
        name =request.post.get("name")
        DataInput = Contact.objects.filter(Q(name_icontains=Data))
        context = {}
