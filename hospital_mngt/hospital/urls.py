from django.urls import path
from hospital.views import About,Home,Contact,Login,Logout,Index,View_doctor,Delete_doctor,Add_doctor,Add_patient,View_patient,Delete_patient,View_appointment,Add_appointment,Delete_appointment,View_nurse,Add_nurse,Delete_nurse

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('index/', Index, name='index'),
    
    path('add_doctor/', Add_doctor, name='add_doctor'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('delete_doctor/<int:dId>/', Delete_doctor, name='delete_doctor'),
    
    path('add_nurse/', Add_nurse, name='add_nurse'),
    path('view_nurse/', View_nurse, name='view_nurse'),
    path('delete_nurse/<int:dId>/', Delete_nurse, name='delete_nurse'),
    
    path('add_patient/', Add_patient, name='add_patient'),
    path('view_patient/', View_patient,name='view_patient'),
    path('delete_patient/<int:pId>/', Delete_patient, name='delete_patient'),
    
    path('add_appointment/', Add_appointment, name='add_appointment'),
    path('view_appointment/',View_appointment, name='view_appointment'),
    path('delete_appointment/<int:apId>/', Delete_appointment, name='delete_appointment'),

]