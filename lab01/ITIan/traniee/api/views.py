from django import views
from django.db.models import query
from django.http import JsonResponse,HttpResponse

from rest_framework.response import Response
from rest_framework import status
from  rest_framework.decorators import api_view,permission_classes

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView, get_object_or_404

from traniee.models import *
from .serlizer import *
from rest_framework import viewsets



class Tranieeviewset(viewsets.ViewSet):
    
    def list(self,request):
        queryset=Traniee.objects.select_related('Course').all()
        serializer=TranieeSerlizer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serlizer=TranieeSerlizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response(data=serlizer.data,status=status.HTTP_201_CREATED)
        return  Response(serlizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):
        queryset=Traniee.objects.select_related('Course').all()
        traniee=get_object_or_404(queryset,pk=pk)
        tranieeser=TranieeSerlizer(traniee)
        return Response(data=tranieeser.data,status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        traniee=get_object_or_404(Traniee,pk=pk)
        serializer=TranieeSerlizer(instance=traniee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        traniee = get_object_or_404(Traniee, pk=pk)
        serializer = TranieeSerlizer(instance=traniee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        traniee = get_object_or_404(Traniee, pk=pk)
        traniee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
