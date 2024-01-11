from django.shortcuts import render,redirect
from .models import Account,BusinessManager,BusinessEmployee
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        password=request.POST['password']


        user=Account.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone_number=phone_number,
            password=make_password(password),
            is_active=True
          
        )

        return render(request,'registration_pending.html')
        

    return render(request,'register.html')



def userlogin(request):

    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST['password']
      

        user=authenticate(username=email,password=password)
        print(user)
        try:
            if user:
                return redirect('home')
        except ObjectDoesNotExist:
           print('user not exixt')

    return render(request,'sign-in.html')

        

    




def adminPage(request):
    user=Account.objects.filter(is_superadmin=False)
    for users in user:
        print(users)
    
    return render(request,'adminPage.html',{'user':user})





