from traniee.views import *
from django.urls import path
urlpatterns = [
path('', tranieeList.as_view(), name='traineelist'),
path('update/<int:id>/', updatetrainee, name='updatetrainee'),
path('delete/<int:id>/', deletetrainee, name='deletetrainee'),
path('home/', addtraniee.as_view(), name='home'),
path('<int:id>/', gettranieebyid, name='traniee_get'),

path('HDelete/<int:id>/',Hardtranieedelete,name='HTraniee_delete'),
path('SDelete/<int:id>/',softtranieedelete,name='STraniee_delete'),
]