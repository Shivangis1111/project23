from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Leave,Student,OTP,Visitors,Hod,Warden,Parents,User])