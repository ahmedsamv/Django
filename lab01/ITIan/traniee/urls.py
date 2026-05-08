from traniee.views import *
from django.urls import path
urlpatterns = [
path('', listtrainee, name='traineelist'),
path('add/', addtrainee, name='addtrainee'),
path('update/<int:id>/', updatetrainee, name='updatetrainee'),
path('delete/<int:id>/', deletetrainee, name='deletetrainee'),
path('home/', home, name='home'),
path('<int:id>/', gettranieebyid, name='traniee_get'),


]