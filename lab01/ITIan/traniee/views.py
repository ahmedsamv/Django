from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def listtrainee(request):
    #return HttpResponse("<h1> list of traniee </h1>")
    return render(request,"trainee/list.html")


def addtrainee(request):
    return HttpResponse("<h1> add trainee </h1>")

def updatetrainee(request,id):
    return HttpResponse(f"<h1> update trainee {id} </h1>")

def deletetrainee(request,id):
    return HttpResponse(f"<h1> delete trainee {id} </h1>")

