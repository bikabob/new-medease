from django.shortcuts import render,redirect
from .forms import PharmacyForm
from .models import Pharmacy


def Pharmacy_register(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-view")
    else:
        form = PharmacyForm()
    context={
        "form":form
    }
    return render(request,'pharmacy/index.html',context=context)
