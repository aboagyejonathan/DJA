from django.shortcuts import render

from .models import Product


# Create your views here.
def Home (request):
    Products = Product.objects.filter(type='sports')
    Products1 = Product.objects.filter(type='board')
    contexts={"keyInView": Products,"keyInBoard": Products1}

    return render(request,'Product/index.html',contexts)



def Atheletics (request):
    
    return render(request,'Product/athletics.html',{"key":"Data from Database"})

def About (request):

    return render(request,'Product/about.html',{"key":"Data from Database"})

def Calendar (request):

    return render(request,'Product/calendar.html',{"key":"Data from Database"})

def Chamb (request):
    # Products = Product.objects.all()
    Products = Product.objects.filter(type='entertament')

    return render(request,'Product/chamb.html',{"keyInView": Products})

def Course (request):

    return render(request,'Product/course.html',{"key":"Data from Database"})

def Media (request):

    return render(request,'Product/media.html',{"key":"Data from Database"})

def Mission (request):

    return render(request,'Product/mission.html',{"key":"Data from Database"})

def Enroll (request):

    return render(request,'Product/enroll.html',{"key":"Data from Database"})

def DailySchedules (request):

    return render(request,'Product/schedules.html',{"key":"Data from Database"})

def Register (request):

    return render(request,'Product/register.html',{"key":"Data from Database"})

def Dining (request):

    return render(request,'Product/dining.html',{"key":"Data from Database"})

def Family (request):

    return render(request,'Product/family.html',{"key":"Data from Database"})

def Post (request):

    return render(request,'Product/post.html',{"key":"Data from Database"})

def Gov (request):

    return render(request,'Product/gov.html',{"key":"Data from Database"})

def Service (request):

    return render(request,'Product/service.html',{"key":"Data from Database"})

def State (request):

    return render(request,'Product/statement.html',{"key":"Data from Database"})

def Rules (request):

    return render(request,'Product/rules.html',{"key":"Data from Database"})

def More (request):

    return render(request,'Product/more.html',{"key":"Data from Database"})

def Read (request):

    return render(request,'Product/read.html',{"key":"Data from Database"})

def Employment (request):

    return render(request,'Product/employment.html',{"key":"Data from Database"})

def Dona (request):

    return render(request,'Product/dona.html',{"key":"Data from Database"})




