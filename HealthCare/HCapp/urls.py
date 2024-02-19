from django.urls import path
from . import views
urlpatterns = [
path('home/',views.home,name="home"),
path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path('service/',views.service,name="service"),
path('register_patient/',views.register_patient,name="register_patient"),
path('register_doctor/',views.register_doctor,name="register_doctor"),
path('appointment_requested/',views.appointment_requested,name="appointment_requested"),
path('loginuser/',views.loginuser,name="loginuser"),
path('logoutuser/',views.logoutuser,name="logoutuser"),
path('viewdoctor/',views.viewdoctor,name="viewdoctor"),
path('viewpatient/',views.viewpatient,name="viewpatient"),
path('viewappointment/',views.viewappointment,name="viewappointment"),
]