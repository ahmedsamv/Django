from django.urls import path, include
from .views import *

from rest_framework.routers import SimpleRouter,DefaultRouter


drouter=DefaultRouter()
drouter.register(r'VS',Tranieeviewset,basename='VS')


crouter=DefaultRouter()
crouter.register(r'CourseVS',Courseviewset,basename='CourseVS')

urlpatterns = [
 path('',include(drouter.urls)),
 
 path('',include(crouter.urls)),

]