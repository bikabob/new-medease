from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import SubmitPrescription
from .models import Prescriptions
from hospital.models import PatientDetails


def submit_prescription(request):
    if request.method == "POST":
        form = SubmitPrescription(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token_number']
            try:
                patient = PatientDetails.objects.get(token_number=token)
                doctor = patient.doctor
                hospital = patient.hospital

                instance = Prescriptions.objects.create(
                    patient=patient,
                    doctor=doctor,
                    hospital=hospital,
                    text=form.cleaned_data['text']
                )
                instance.save()

                return redirect('prescription_success')  
            except PatientDetails.DoesNotExist:
                form.add_error('token_number', 'Invalid token number. Patient not found.')
    else:
        form = SubmitPrescription()
    
    
    return render(request, 'prescription/index.html', {'form': form})

def view_prescription(request, tokenNumber):
    try:
        patient = PatientDetails.objects.get(token_number=tokenNumber)
        context = {
            'status': "success",
            "data": {
                "patient": patient.name,
                "age": patient.age,  # Ensure you have this field
                "date_of_birth": patient.dob,  # Ensure you have this field
                "contact": patient.contact,  # Ensure you have this field
            }
        }
        return JsonResponse(context)
    except PatientDetails.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Patient not found."}, status=404)
