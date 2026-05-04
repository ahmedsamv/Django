from course.views import *
from django.urls import path

urlpatterns = [
path('', listcourse, name='courselist'),
path('add/', addcourse, name='addcourse'),
path('update/<int:id>/', updatecourse, name='updatecourse'),
path('delete/<int:id>/', deletecourse, name='deletecourse'),

]