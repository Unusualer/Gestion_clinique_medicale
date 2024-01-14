from django.urls import path
from hospital.views import About,Home,Contact,Login,Logout,Index
from hospital.views import Add_doctor,View_doctor,Edit_doctor,Delete_doctor
from hospital.views import Add_patient,View_patient,Edit_patient,Delete_patient
from hospital.views import Add_appointment,View_appointment,Edit_appointment,Delete_appointment
from hospital.views import Add_nurse,View_nurse,Edit_nurse,Delete_nurse


urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('index/', Index, name='index'),
    
    path('add_doctor/', Add_doctor, name='add_doctor'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('edit_doctor/<int:dId>/', Edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:dId>/', Delete_doctor, name='delete_doctor'),
    
    path('add_nurse/', Add_nurse, name='add_nurse'),
    path('view_nurse/', View_nurse, name='view_nurse'),
    path('edit_nurse/<int:nId>/', Edit_nurse, name='edit_nurse'),
    path('delete_nurse/<int:nId>/', Delete_nurse, name='delete_nurse'),
    
    path('add_patient/', Add_patient, name='add_patient'),
    path('view_patient/', View_patient,name='view_patient'),
    path('edit_patient/<int:pId>/', Edit_patient, name='edit_patient'),
    path('delete_patient/<int:pId>/', Delete_patient, name='delete_patient'),
    
    path('add_appointment/', Add_appointment, name='add_appointment'),
    path('view_appointment/',View_appointment, name='view_appointment'),
    path('edit_appointment/<int:apId>/', Edit_appointment, name='edit_appointment'),
    path('delete_appointment/<int:apId>/', Delete_appointment, name='delete_appointment'),

]