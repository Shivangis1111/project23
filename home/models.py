from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from django.utils.timezone import now
import datetime

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1,'parent'),
        (2,'hod'),
        (3,'warden')
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=1)


class Student(models.Model):
    s_class=models.CharField(max_length=40)
    hostel=models.CharField(max_length=30)
    s_name=models.CharField(max_length=50)
    s_id=models.CharField(max_length=12)
    s_email=models.EmailField()
    p_name=models.CharField(max_length=50)
    p_number=models.IntegerField(default='1234567799')
    s_number=models.IntegerField()
    p_email=models.EmailField()
    no_of_days_left=models.IntegerField()
    s_roll=models.IntegerField(null=True)

    #def __init__(self):
        #return self.s_name

class Parents(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    s_id=models.CharField(max_length=12)
    p_number=models.IntegerField(default='1234567799')

class Visitors(models.Model):
    s_id=models.CharField(max_length=12)
    arr_date=models.DateField()
    vehicle_no=models.CharField(max_length=10)
    no_of_visitors=models.IntegerField()
    visitors_relation=models.CharField(max_length=20)
    visitor_name = models.CharField(max_length=50,default='None')
    code = models.ImageField(upload_to='code',blank=True)

    def __str__(self) -> str:
      return self.s_id
    
    
    #def save(self,*args,**kwargs):
        #combined = f'Student ID:{self.s_id}\nName:{self.visitor_name}\nRealtion:{self.visitors_relation}\nVehicle Number:{self.vehicle_no}\nDate:{self.arr_date}'
        #qrcode_img = qrcode.make(combined)
        #qrcode_offset = Image.new("RGB", (400,400),"white")
        #qrcode_offset.paste(qrcode_img)
        #stream = BytesIO()
        #qrcode_offset.save(stream,"PNG")
        #self.code.save(f'{self.s_id}_{self.arr_date}.png',File(stream),save=False)
        #qrcode_offset.close()
        #super().save(*args,**kwargs)
    

class Hod(models.Model):
    h_name=models.CharField(max_length=50)
    h_dept=models.CharField(max_length=30)
    

class Warden(models.Model):
    w_name=models.CharField(max_length=50)
    hostel_name=models.CharField(max_length=30)
   

# class QR(models.Model):
#     unique_no=models.CharField(max_length=20)
#     created_at=models.DateField()

class Leave(models.Model):
    s_name = models.CharField(max_length=50,default='None')
    s_id=models.CharField(max_length=12)
    s_date=models.DateField()
    e_date=models.DateField()
    nod=models.IntegerField()
    go_alone=models.BooleanField()
    reason=models.TextField()
    person_name=models.CharField(max_length=50,null=True,blank=True)
    relation=models.CharField(max_length=25,null=True,blank=True)
    per_add=models.CharField(max_length=60,null=True,blank=True)
    per_pno=models.CharField(max_length = 10,null=True,blank=True)
    is_approved=models.IntegerField(default=0)
    gatepass_generated = models.BooleanField(default=False)
    def __str__(self) -> str:
        return super().__str__()
        
    
class OTP(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    otp=models.IntegerField()