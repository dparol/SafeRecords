from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class MyAccountManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('you must have an email address')
        
        if not username:
            raise ValueError('user must have an username')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,first_name,last_name,email,username,password):

        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser, PermissionsMixin):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=50)


    date_joined =models.DateTimeField(auto_now_add=True)
    last_joined =models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager()


    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    

    def has_module_perms(self, app_label):
        return self.is_admin
        



class BusinessManager(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    managerId=models.CharField(max_length=50)


class BusinessEmployee(models.Model):
    managerid=models.ForeignKey(BusinessManager,on_delete=models.CASCADE)
    emp_id=models.CharField(max_length=50)
    emp_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    emp_IdCard=models.ImageField(upload_to=None)

quality_choice=(
         
         ('good','GOOD'),
         ('damaged','Damaged')
         )
item_status=(
    ('checked','CHECKED'),
    ('unchecked','UNCHECKED')
)
class Barcode_Data(models.Model):
    empId=models.ForeignKey(BusinessEmployee,on_delete=models.CASCADE)
    room_number=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    item_name=models.CharField(max_length=50)
    item_id=models.CharField(max_length=50)
    quality=models.CharField(max_length=100,choices=quality_choice)
    com_note=models.TextField(max_length=100)
    item_status=models.CharField(max_length=50,choices=item_status,default="unckecked")

