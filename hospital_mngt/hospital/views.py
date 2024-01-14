from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Doctor,Patient,Appointment,Nurse
def About(request):
    active_page = 'about'
    return render(request, 'about.html', {'active_page': active_page})

def Home(request):
    active_page = 'home'
    return render(request, 'home.html', {'active_page': active_page})

def Contact(request):
    active_page = 'contact'
    return render(request, 'contact.html', {'active_page': active_page})

def Index(request):
    active_page = 'index'
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html', {'active_page': active_page})


def Login(request):
    active_page = 'login'
    error = ""
    if request.method == "POST":
        u = request.POST.get('uname', '')
        p = request.POST.get('pwd', '')
        
        try:
            user = authenticate(username=u, password=p)
            
            if user is not None and user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            # Handle specific exceptions if needed
            print(f"Exception: {e}")
            error = "yes"
            
    d = {'error': error}
    #return render(request, 'login.html', d)   
    #return render(request, 'login.html', {'active_page': active_page})
    return render(request, 'login.html', {**d, 'active_page': active_page})

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_doctor(request):
    active_page = 'doctor'
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    doc = {'doctors' : doctors}
    return render(request, 'view_doctor.html', {**doc, 'active_page': active_page})

def Add_doctor(request):
    error = ""
    active_page = 'doctor'
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST.get('name', '')
        p = request.POST.get('phone', '')
        sp = request.POST.get('sp', '')
        try:
            Doctor.objects.create(Name=n, Phone=p, SP=sp)
            error = "no"
        except:
            error = "yes"
            
    e = {'error': error}
    return render(request, 'add_doctor.html', {**e, 'active_page': active_page})

def Delete_doctor(request, dId):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.get(id = dId)
    doctors.delete()
    return redirect('view_doctor')

def View_nurse(request):
    active_page = 'nurse'
    if not request.user.is_staff:
        return redirect('login')
    nurses = Nurse.objects.all()
    doc = {'nurses' : nurses}
    return render(request, 'view_nurse.html', {**doc, 'active_page': active_page})

def Add_nurse(request):
    error = ""
    active_page = 'nurse'
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST.get('name', '')
        p = request.POST.get('phone', '')
        sp = request.POST.get('sp', '')
        try:
            Doctor.objects.create(Name=n, Phone=p, SP=sp)
            error = "no"
        except:
            error = "yes"
            
    e = {'error': error}
    return render(request, 'add_nurse.html', {**e, 'active_page': active_page})

def Delete_nurse(request, dId):
    if not request.user.is_staff:
        return redirect('login')
    nurses = Nurse.objects.get(id = dId)
    nurses.delete()
    return redirect('view_nurse')

def View_patient(request):
    active_page = 'patient'
    if not request.user.is_staff:
        return redirect('login')
    patients = Patient.objects.all()
    p = {'patients' : patients}
    return render(request,'view_patient.html',{**p,'active_page' : active_page})

def Add_patient(request):
    active_page = 'patient'
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST.get('name','')
        g = request.POST.get('gender','')
        p = request.POST.get('phone','')
        a = request.POST.get('address','')
        try:
            Patient.objects.create(Name=n,Gender=g,Phone=p,Address=a)
            error = "no"
        except:
            error = "yes"
    e = {'error' : error}
    return render(request, 'add_patient.html',{**e,'active_page' : active_page})

def Delete_patient(request,pId):
    if not request.user.is_staff:
        return redirect('login')
    patients = Patient.objects.get(id = pId)
    patients.delete()
    return redirect('view_patient')
    
def View_appointment(request):
    active_page = 'appointment'
    if not request.user.is_staff:
        return redirect('login')
    appointments = Appointment.objects.all()
    ap = {'appointments' : appointments}
    return render(request,'view_appointment.html',{**ap,'active_page' : active_page})

def Add_appointment(request):
    active_page = 'appointment'
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    pat = Patient.objects.all()
    if request.method == "POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        dt = request.POST['date']
        t = request.POST['time']
        doctors = Doctor.objects.filter(Name=d).first()
        patients = Patient.objects.filter(Name=p).first()
        try:
            Appointment.objects.create(Doctor=doctors,Patient=patients,Date=dt,time=t)
            error = "no"
        except:
            error = "yes"
    e = {'doctors' : doc ,'patients' : pat , 'error' : error }
    return render(request, 'add_appointment.html',{**e,'active_page' : active_page})

def Delete_appointment(request,apId):
    if not request.user.is_staff:
        return redirect('login')
    appointments = Appointment.objects.get(id = apId)
    appointments.delete()
    return redirect('view_appointment')