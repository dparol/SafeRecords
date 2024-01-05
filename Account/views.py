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
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)

        try:
            user=Account.objects.get(Q(username__iexact=username))
        except ObjectDoesNotExist:
            user = None

        if user is not None and check_password(password,user.password):
            login(request, user)
            if user is not None and user.is_superadmin:
                return render(request,'adminPage.html')
            elif user is not None and user.is_admin:
                message={"message":"please wait until admin approves"}
                return render(request,'registration_pending.html',{'message':message})
            elif user is not None and user.is_active:
                return render(request,'registration_pending.html') 
            else:
                messages.error(request,"invalid login credentials")
        else:
                messages.error(request,"invalid login credentials")
    return render(request,'sign-in.html')

        

    

def approve_registration(request):

    user_id=

    #take single manager data and processing
    user=Account.objects.get(pk=user_id)
    #to allow all permissions
    user.is_active=True
    user.is_staff=True
    user.is_admin=True
    #save data
    user.save()
    
    #create new manager id
    # manager=BusinessManager.objects.get(user=user)
    #to provide manager id in database
    # manager.managerId=manager_id
    # #save data
    # manager.save()

    return render(request,'registration_approved.html')


def adminPage(request):
    user=Account.objects.filter(is_superadmin=False)
    for users in user:
        print(users)
    create_new_employee=Newemployee()
    return render(request,'adminPage.html',{'user':user})



def Newemployee(request):
    if request.method == 'POST':
        emp_id=request.POST['emp_id']
        emp_name=request.POST['emp_name']
        phone_number=request.POST[phone_number]
        emp_IdCard=request.POST[emp_IdCard]

        new_employee=BusinessEmployee.objects.create(
            emp_id=emp_id,
            emp_name=emp_name,
            phone_number=phone_number,
            emp_IdCard=emp_IdCard
        )

        return render(request,'create_new_employee.html')


