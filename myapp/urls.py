from django.urls import path, include
from myapp import views


urlpatterns = [
    path("" , views.home),
    path('login' , views.login),
    path('signup',views.handleSignup),
    path('verify/token' , views.verifytoken)
]
