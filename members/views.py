from django.shortcuts import render
from .models import Member
# from django.http import HttpResponse
# from django.template import loader
# import requests

# def welcome(request):
#     return HttpResponse("HI Everyone am ukpono andem,A programmer")

# def about(request):
#     return render(request, "about.html")

def Home(request):
    members = Member.objects.all()
    print(members)
    return render(request, "Home.html", {"members":members})

def about(request):
    members = Member.objects.all()  # Fetch all members
    return render(request, "about.html", {"mymembers": members})

def details(request, id):
    member = Member.objects.get(id=id)  # Fetch a specific member based on ID
    return render(request, "details.html", {"member": member})

def testing(request):
    context = {
   'firstname': 'Ukpono',
    'lastname':  'Andem'
    }

    return render(request, 'testing.html', context )


def newpage(request):
    context = {
        'Name': 'mercy chinwo',
         'age':  '23',
         'email':'ukponoadem@gmail.com',
         'phone_num':'09161248397',
         'date-of-birth':'2012-12-15'
    }
    return render(request,'')

# Create your views here.



# def about(request):
#   template = loader.get_template('about.html')
#   return HttpResponse(template.render())