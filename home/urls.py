from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login,name='login'),
   path('hod-d/',views.hod,name='login2'),
   path('warden-d/',views.warden,name='login3'),
   path('otp-p/',views.otp_p,name='otpp'),
   path('otp-check/',views.check_otp,name='checkotp'),
   path('leave/',views.leave,name='leave'),
   path('parent-d/',views.dash,name='dash'),
   path('leave-request/',views.accepted,name='accept'),
   path('stud/<str:i_id>',views.stud_approve,name='stud'),
   path('stude/<str:i__id>',views.stud_reject,name='stude'),
   path('visitor/',views.visit,name='visit'),
   path('generate/<str:i_id>',views.generate,name='generate'),
   path('logout/',views.logout_view,name='logout'),
   path('logout1/',views.logout_view1,name='logout1'),
   path('logout2/',views.logout_view2,name='logout2')
]