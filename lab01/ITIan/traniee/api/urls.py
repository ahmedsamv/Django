from django.urls import path, include
from .views import *

from rest_framework.routers import SimpleRouter,DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

drouter=DefaultRouter()
drouter.register(r'VS',Tranieeviewset,basename='VS')


crouter=DefaultRouter()
crouter.register(r'CourseVS',Courseviewset,basename='CourseVS')


urlpatterns = [
path('',include(drouter.urls)),
 
path('',include(crouter.urls)),

#jwt
# Login: Returns Access and Refresh tokens
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

# Refresh: Returns a new Access token using the Refresh token
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]