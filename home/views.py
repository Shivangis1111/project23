from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
import random,time
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def home(request):
    return render(request,'home.html')

def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password'] 
        user=auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request,user) 
            if user.is_authenticated:
                otp=random.randint(1000,9999)
                otp_data = OTP(user=request.user,otp=otp)
                otp_data.save()
                account_sid = 'AC5181b41513de4cd62d6e51f7f6aee877'
                auth_token = 'cfe3d3c3e0080e437b6217aed72ad2ec'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+14752629306',
                body=f'Your OTP is : {otp}',
                to='+916290991225'
                )
                return redirect('otpp')
        else: 
                messages.info(request,'Credentials Invalid')
                return redirect('login')
    return render(request,'login.html')
            


def parent(request):
    return render(request,'parent_d.html')


def otp_p(request):
    return render(request,'otp_p.html')


    

@login_required
def leave(request):
    stu_name = Student.objects.filter(s_id=request.user)
    context = {'data' : stu_name}
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_id = request.POST['s_id']
        reason = request.POST['reason']
        s_date = request.POST['s_date']
        s_date = str(s_date)
        e_date = request.POST['e_date']
        e_date = str(e_date)
        go_alone = request.POST['go_alone']
        nod = request.POST['nod']
        person_name = request.POST['person_name']
        relation = request.POST['relation']
        per_add = request.POST['per_add']
        per_pno = request.POST['per_pno']
        leave = Leave(s_name=s_name,s_id=s_id,s_date=s_date,e_date=e_date,nod=nod,go_alone=go_alone,reason=reason,person_name=person_name,relation=relation,per_add=per_add,per_pno=per_pno)
        leave.save()
        return redirect('dash')
    return render(request,'leave.html',context)

@login_required
def dash(request):
    stu_name=Student.objects.filter(s_id=request.user).order_by('-id')
    lea = Leave.objects.filter(s_id=request.user).order_by('-id')
    context = {'data' : stu_name,
               'data1' : lea}
    return render(request,'parent_d.html',context)


@login_required
def hod(request):
    data = Leave.objects.order_by('-id')
    context = {'data' : data}
    return render(request,"hod_d.html",context)
    


def accepted(request):
    if request.method=='POST':
        is_approved = request.POST['is_approved']
        user = request.user
        lea = user.Leave(is_approved=is_approved)
        lea.save()
    return redirect('login2')


def stud_approve(request,i_id):
    i = Leave.objects.get(id=i_id)
    i.is_approved = 1
    i.save()
    return redirect('login2')

def stud_reject(request,i__id):
    i = Leave.objects.get(id=i__id)
    i.is_approved = 2
    i.save()
    send_mail(
        'Leave Rejected',
        'Respected Parent \nYour application for leave has been rejected.\nPlease contact the respective department for the reason for the same.\nRegards\nBanasthali Vidyapith',
        '0809neha2002@gmail.com',
        ['shivangisharma110204@gmail.com'],
        fail_silently=False,
    )
    return redirect('login2')

@login_required
def warden(request):
    data = Leave.objects.order_by('-id')
    data1 = {'data' : data}
    return render(request,'warden_d.html',data1)


def visit(request):
    if request.method == 'POST':
        s_id = request.POST['s_id']
        arr_date = request.POST['arr_date']
        vehicle_no  = request.POST['vehicle_no']
        no_of_visitors = request.POST['no_of_visitors']
        visitors_relation = request.POST['visitors_relation']
        visitor_name = request.POST['visitor_name']
        visits = Visitors(s_id=s_id,arr_date=arr_date,vehicle_no=vehicle_no,no_of_visitors=no_of_visitors,visitors_relation=visitors_relation,visitor_name=visitor_name)
        visits.save()
        img = qrcode.make("Smart ID :"+ s_id+"\nName : "+visitor_name+"\nVehicle number : "+vehicle_no+"\nArriving date : "+arr_date+"\nRelation : "+visitors_relation+"\nNumber of visitors : "+no_of_visitors)
        img_name = s_id + arr_date + '.png'
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        
        img_path = Image.open("D:/project23(2)/project/media/"+img_name)
        img_path = img_path.convert('RGB')
        img_path.save("D:/project23(2)/project/media/"+img_name+".pdf",format="PDF")
        email = EmailMessage('Visitors slip','Respected Visitor,\nYour visitor slip is attached hereby.','0809neha2002@gmail.com',['shivangisharma110204@gmail.com'])
        email.attach_file('D:/project23(2)/project/media/'+img_name+'.pdf')
        email.send()
        return redirect('dash')


def generate(request,i_id):
    i = Leave.objects.get(id=i_id)
    i.gatepass_generated = 'True'
    i.save()

    id = i.s_id
    name = i.s_name
    sdate = i.s_date
    edate = i.e_date
    nods = i.nod
    img = qrcode.make("Smart ID :"+str(id)+"\nName : "+name+"\nFrom : "+str(sdate)+"\nTo : "+str(edate)+"\nNumber of days : "+str(nods))
    img_name = id + name + '.png'
    img.save(settings.MEDIA_ROOT + '/' + img_name)
    img_path = Image.open("D:/project23(2)/project/media/"+img_name)
    img_path = img_path.convert('RGB')
    img_path.save("D:/project23(2)/project/media/"+img_name+".pdf",format="PDF")
    email = EmailMessage('Gatepass','Dear Student\nYour gatepass is attached hereby.','0809neha2002@gmail.com',['shivangisharma110204@gmail.com'])
    email.attach_file('D:/project23(2)/project/media/'+img_name+'.pdf')
    email.send()
    return redirect("login3")



def check_otp(request):
    if request.method == 'POST':
        user_otp = request.POST['user_otp']
    otp = OTP.objects.get(user=request.user)
    user=User.objects.get(id=request.user.id)
    print(type(otp.otp),user.user_type,type(user_otp))
    if otp.otp == int(user_otp) and user.user_type == 1:
        print("hello")
        return redirect('dash')
    elif otp.otp == int(user_otp) and user.user_type == 2:
        return redirect('login2')
    elif otp.otp == int(user_otp) and user.user_type == 3:
        return redirect('login3')
    else:
        return redirect('login')
    

def logout_view(request):
    logout(request)
    return redirect('home')

def logout_view1(request):
    logout(request)
    return redirect('home')

def logout_view2(request):
    logout(request)
    return redirect('home')