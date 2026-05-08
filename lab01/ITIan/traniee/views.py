from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from pip._internal import req
from .models import *

# Create your views here.


def listtrainee(request):
    #return HttpResponse("<h1> list of traniee </h1>")
    context={'name':'itian','traniees':Traniee.objects.all()}

    return render(request,"trainee/list.html",context)

def addtrainee(request):
    return HttpResponse("<h1> add trainee </h1>")

def updatetrainee(request,id):
    return HttpResponse(f"<h1> update trainee {id} </h1>")

def deletetrainee(request,id):
    return HttpResponse(f"<h1> delete trainee {id} </h1>")

# def home(request):
#     Traniees = Traniee.objects.all() 
#     return render(request,"trainee/home.html",{"Traniees":Traniees})


def home(request):
        # return HttpResponse(f'<h1>book add</h1>')
    if request.method == 'POST':

        Traniee.objects.create(
            id=request.POST['tid'],
            name=request.POST['tname'],
            email=request.POST['temail'],
            fees=request.POST['fees'],
        )
        return redirect ('traineelist')
    return render (request,'trainee/home.html')


def gettranieebyid(request,id):
    context={'traniee':Traniee.objects.get(id=id)}
    return render(request,'trainee/tranieedetails.html',context)


def Hardtranieedelete(request,id):
  
    if (Traniee.objects.filter(pk=id) ):
        
        Traniee.objects.filter(id=id).delete()
    
        return redirect('traineelist')
    # else:
    else:
        return render(request,'trainee/list.html',context={'error':'traniee not found'})