from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
   return HttpResponse("My second app")

def help(request):
    help_dict = {'help_insert':"Welcome to the help page from views.py!!"}
    return render(request,'app_2_template/help.html',context=help_dict)
