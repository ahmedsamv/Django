from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from pip._internal import req

from .models import *

from .forms import *

from django.views import View
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy


# Create your views here.

class tranieeList(ListView):
    queryset=Traniee.objects.filter(is_active=True)
    model=Traniee
    template_name='trainee/list.html'
    context_object_name='traniees'


def listtrainee(request):
    #return HttpResponse("<h1> list of traniee </h1>")
    context={'name':'itian','traniees':Traniee.objects.filter(is_active=True)}

    return render(request,"trainee/list.html",context)


def updatetrainee(req,id):
    context={'form':TranieeModelForm(instance=Traniee.objects.get(id=id))}
    if req.method=='POST':
        form=TranieeModelForm(req.POST,req.FILES,instance=Traniee.objects.get(id=id))
        if(form.is_valid()):
            form.save()
            return redirect('traineelist')
        else:
            context['error']=form.errors
            return render(req, 'trainee/update.html' , context)
    return render(req, 'trainee/update.html' , context)



def deletetrainee(request,id):
    return HttpResponse(f"<h1> delete trainee {id} </h1>")

# def home(request):
#     Traniees = Traniee.objects.all() 
#     return render(request,"trainee/home.html",{"Traniees":Traniees})


class addtraniee(CreateView):
    model=Traniee
    fields = ['id', 'name', 'email', 'fees', 'Traniee_image', 'Course']
    template_name='trainee/home.html'
    success_url=reverse_lazy('traineelist')




class newhome(View):
        
        context = {'course': Course.objects.all(),'form':TranieeModelForm()}
        def get(self,request):
           
            return render (request,'trainee/home.html',newhome.context)
        def post(self,request):
            form=TranieeModelForm(data=request.POST,files=request.FILES)
            if(form.is_valid()):
                form.save()
            return redirect ('traineelist')



def home(request):
    context = {'course': Course.objects.all(),'form':TranieeModelForm()}
        # return HttpResponse(f'<h1>book add</h1>')
    if request.method == 'POST':

        form=TranieeModelForm(data=request.POST,files=request.FILES)
        if(form.is_valid()):
            form.save()
            # Traniee.objects.create(
            #     id=request.POST['id'],
            #     name=request.POST['name'],
            #     email=request.POST['email'],
            #     fees=request.POST['fees'],
            #     Traniee_image=request.FILES.get("Traniee_image"),
            #     Course=Course.objects.get(pk=request.POST['Course'])
            # ) 
        # Traniee.objects.create(
        #     id=request.POST['tid'],
        #     name=request.POST['tname'],
        #     email=request.POST['temail'],
        #     fees=request.POST['fees'],
        # )
        return redirect ('traineelist')
    return render (request,'trainee/home.html',context)


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
    

def softtranieedelete(request,id):
    Traniee.objects.filter(id=id).update(is_active=False)
    return redirect('traineelist')