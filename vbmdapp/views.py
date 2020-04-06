from django.core import mail
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Patient
from datetime import date
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
import pdfkit


# home_view


def home(request):
    return render(request, 'mainPage.html')


# admin_view

def admin(request):
    return render(request, 'admin.html')


# doctors_record_view

def doctors_record(request):
    doct_list = Doctor.objects.all()
    context = {
        'doctors_record': doct_list
    }
    return render(request, 'doctors_record.html', context)

# patients_record_view


def patients_record(request):
    pat_list = Patient.objects.all()
    context = {
        'patients_record': pat_list
    }
    return render(request, 'patients_record.html', context)

# doctors_entry_form


def doctors_entry(request):
    if request.method == "POST":

        doc_name = request.POST['docName']
        doc_spec = request.POST['splstIn']
        doc_gender = request.POST['gender']
        doc_mobile = request.POST['docMobile']
        doc_location = request.POST['docLocality']

        doctor = Doctor(doctor_name=doc_name, specialist_in=doc_spec,
                        doctor_gender=doc_gender, doctor_mobile_number=doc_mobile, doctor_locality=doc_location)

        doctor.save()
        context = {
            'status': 'Success',
            'message': 'Your Details Stored Successfully :-)'
        }
        return render(request, 'doctors_entry_form.html', context)
    return render(request, 'doctors_entry_form.html')


# patients_entry_form

def patients_entry(request):

    doct_list = Doctor.objects.all()
    context = {
        'doctors_record': doct_list
    }

    if request.method == "POST":

        pat_id = request.POST['patId']
        pat_name = request.POST['patName']
        pat_age = request.POST['patAge']
        pat_gender = request.POST['gender']
        pat_disease = request.POST['patDisease']
        pat_mobile = request.POST['patMobile']
        pat_mail = request.POST['patMail']
        pat_location = request.POST['docLocality']
        pat_doctor = request.POST['patDoc']

        patient = Patient(
            patient_id=pat_id,
            patient_name=pat_name,
            patient_age=pat_age,
            patient_gender=pat_gender,
            patient_disease=pat_disease,
            patient_mob_num=pat_mobile,
            patient_mail=pat_mail,
            patient_locality=pat_location,
            visting_doctor_name=pat_doctor)

        patient.save()
        context = {
            'doctors_record': doct_list,
            'status': 'Success',
            'message': 'Your Details Stored Successfully :-)'
        }
        return render(request, 'patients_entry_form.html', context)
    return render(request, 'patients_entry_form.html', context)


# prescriptionFor

def prescriptionFor(request):
    return render(request, 'prescriptionFor.html')


# prescription

def prescription(request):

    if request.method == "POST":

        # voice_result = request.POST['voiceText']
        presc = []
        patient_id = request.POST['patientIdForPres']

        presc = request.POST['fullPrescription']

        fullPrescription = presc.capitalize()
        today_date = date.today()

        name = Patient.objects.filter(patient_id=patient_id)[0]
        context = {
            'id': patient_id,
            'object': name,
            'presc': fullPrescription,
            'date': today_date

        }

        return render(request, 'prescription.html', context)

# Save as PDF


def Save(request, id):

    fs = FileSystemStorage
    pat_id = id
    file = id+'-Prescription'

    pdfkit.from_file('templates/prescription.html', file+'.pdf')

    # fs.save('original/', pdfFile)

    return HttpResponse('Done')

# Mail Sender


def mailSend(request):

    if request.method == "POST":

        subject = 'Django Test Email'
        body = 'Hey Whats Up !'
        sender = 'silukkusatta1998@gmail.com'
        receiver = 'aambu1998@gmail.com'

        response = send_mail(subject, body, sender, [
                             receiver], fail_silently=False)

        if response == 1:
            context = {
                'status': 'Success',
                'message': 'Mail has been sent successfully.'
            }
            return render(request, 'admin.html', context)
        else:
            context = {
                'status': 'Oops !',
                'message': 'Sorry there was a problem while sending mail.'
            }
            return render(request, 'prescription.html', context)
