from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import ContactForm,PatientRegistrationForm,DoctorRegistrationForm,AppointmentRequestForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import DoctorT,PatientT,AppointT,Contact,AppointCopy


def home(request):
   p = len(PatientT.objects.all())
   d = len(DoctorT.objects.all())
   a =len(AppointT.objects.all())
   return render(request,'index.html',{'p':p,'d':d,'a':a})


def about(request):
    return render(request,'about.html')



def contact(request):
    form  = ContactForm()
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request,"Thank You ! Your record is submitted successfully")
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})
def service(request):
     return render(request,'service.html')



def register_doctor(request):
    form = DoctorRegistrationForm()
    if request.method == 'POST':
        form =DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull")
            return redirect('/loginuser')
    return render(request,'random.html',{'form':form})



def register_patient(request):
    form = PatientRegistrationForm()
    if request.method == 'POST':
        form =PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull")
            return redirect('/loginuser')
    return render(request,'Patient.html',{'form':form})



def loginuser(request):
    if request.method == 'POST':
        name  = request.POST['username']
        password  = request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"{name} ! Welcome to HealthCare")
            return redirect('home')
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginuser')
def doctor_schedule(request):
    doctor = DoctorT.objects.get(user=request.user)
    #appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor_schedule.html')#{'appointments': appointments

@login_required(login_url='loginuser')
def appointment_requested(request):
    pat = PatientT.objects.all()
    doc = DoctorT.objects.all()
    if request.method == 'POST':
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        appoint = AppointCopy(doctor_name=doctor_name,patient_name=patient_name,date=date,time=time)
        appoint.save()
    return render(request, 'appointment_requested.html',{'patient':pat,'doctor':doc})

@login_required(login_url='loginuser')
def viewdoctor(request):
    doctor = DoctorT.objects.all()
    return render(request,'viewdoctor.html',{'doctor':doctor})

@login_required(login_url='loginuser')
def viewpatient(request):
    patient = PatientT.objects.all()
    return render(request,'viewpatient.html',{'patient':patient})

@login_required(login_url='loginuser')
def viewappointment(request):
    appointment = AppointCopy.objects.all()
    return render(request,'viewappointment.html',{'appointment':appointment})