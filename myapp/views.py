from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
  feature1 =Feature()
  feature1.id =0
  feature1.name='fast'
  feature1.dts='its very fast'
  feature2 =Feature()
  feature2.id =1
  feature2.name='relaible'
  feature2.dts='its very relaible'
  feature3 =Feature()
  feature3.id =2
  feature3.name='good'
  feature3.dts='its very good'
  feature4 =Feature()
  feature4.id =3
  feature4.name='helpful'
  feature4.dts='its very helpful'
  fets=[feature1,feature2,feature3,feature4]
  return render(request,'index.html',{'fets':fets })
#def show(request):
#
#     var= request.POST["text"]
  #  return render (request,'result.html',{'result':var})
