from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import login, logout
import jwt



# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return JsonResponse({ 'message' : "You are on the home page" })
    else:
        return JsonResponse({ 'message' : "something went wrong" })



@csrf_exempt
def login(request):
    if request.method == 'POST':
        print("Call has reached")
        email = request.POST['email']
        password = request.POST['password']

        # from db validate this user ==
        context ={
            'myuser' : myuser
        }

        encoded_data =  {  
            'token' :  jwt.encode(context , "this is very complexksncjabjkvbfsk" , algorithm="HS256"),
            'userdata' : context  
        }

        return JsonResponse(encoded_data)
    else:
        return JsonResponse({ 'error' : "something went wrong" })




@csrf_exempt    
def handleSignup(request):
    if request.method == 'POST':
        print('testing...')
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     # return redirect('home')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('home')
        # if (pass1!= pass2):
        #      messages.error(request, " Passwords do not match")
        #      return redirect('home')
        
        # Create the user
        # usermodel = {
        #     
        #     username,
        #     password,
        #     email,
        #     ..
        # }

        # create user in db
        # fetch that user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        print('Registered sucessfully!')
        # make object of the user data ==
        context ={
            'myuser' : myuser
        }

        encoded_data =  {  
            'token' :  jwt.encode(context , "this is very complexksncjabjkvbfsk" , algorithm="HS256"),
            'userdata' : context  
        }
        return JsonResponse(context)
        # return redirect('home')
    else:
        return HttpResponse("404 - Not found")






@csrf_exempt
def verifytoken(request):
    decodedata = jwt.decode(request.META['HTTP_AUTHORIZATION'].split()[1] , "this is very complexksncjabjkvbfsk" , algorithms="HS256")
    id  =  decodedata['myuser']['id']
    # if request.method == "GET":
    #     decodedata = jwt.decode(request.META['HTTP_AUTHORIZATION'].split()[1] , "this is very complexksncjabjkvbfsk" , algorithms="HS256")
    #     if decodedata['id'] == 1:
    #         return JsonResponse({ 'message' : "successfully decoded, User is Authenticated.." , 'payload' : decodedata  })
    #     else:
    #         return JsonResponse({ 'error' : "Authentication is failed" })
    # else:
    #     return JsonResponse({ 'error' : "something went wrong" })



