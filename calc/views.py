from contextlib import nullcontext
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return  render(request,'home.html',{'name':'subin'});
def add(request) :
    var1 =int(request.GET["num1"])

    var2=int (request.GET["num2"])
   
        
    res=var1+var2
    return render (request,'result.html',{'result':res} )   