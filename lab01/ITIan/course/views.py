from django.shortcuts import render
from django.http.response import HttpResponse

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def listcourse(request):
    # return HttpResponse("<h1> list of course </h1>")
    return render(request,"course/list.html")

def addcourse(request):
    return HttpResponse("<h1> add course </h1>")

def updatecourse(request,id):
    return HttpResponse(f"<h1> update course {id} </h1>")   

def deletecourse(request,id):
    return HttpResponse(f"<h1> delete course {id} </h1>")