from django.urls import path
from django.conf.urls import url


from . import views


urlpatterns = [
    path('', views.home, name='mainPage'),
    path('myAdmin', views.admin, name='myAdmin'),
    path('patients_record', views.patients_record, name='patients_record'),
    path('doctors_record', views.doctors_record, name='doctors_record'),
    path('doctors_entry', views.doctors_entry, name='doctors_entry'),
    path('patients_entry', views.patients_entry, name='patients_entry'),
    path('prescriptionFor', views.prescriptionFor, name='prescriptionFor'),
    path('prescription', views.prescription, name='prescription'),
    url(r'^mailSend/(?P<id>[-\w.]+\w{0,50})/$',
        views.mailSend, name='mailSend'),
]
