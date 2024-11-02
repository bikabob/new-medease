from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import SubmitPrescription
from .models import Prescription
from hospital.models import PatientDetails

def submit_prescription(request):
    if request.method == "POST":
        form = SubmitPrescription(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token_number']
            patient = PatientDetails.objects.get(token_number=token)
            doctor = patient.doctor
            hospital = patient.hospital


            instance = Prescription.objects.create(
                patient=patient,
                doctor=doctor,
                hospital=hospital,
                text=form.cleaned_data['text']
            )
            instance.save()

            
            return redirect('prescription_success')  

    else:
        form = SubmitPrescription()
    return render(request, 'prescription/index.html', {'form': form})

def view_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    context = {
        'status': "success",
        "data": {
            "patient": prescription.patient.name,
            "doctor": prescription.doctor.name,
            "hospital": prescription.hospital.name,
            "text": prescription.text,
            "date": prescription.date,
        }
    }
    return JsonResponse(context)