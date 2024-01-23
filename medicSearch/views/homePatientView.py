from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login-patient/')
def home_patient(request):
    return render(request, template_name='homePatient.html', status=200)
