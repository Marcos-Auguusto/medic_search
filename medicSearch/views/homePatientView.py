from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, template_name='homePatient.html', status=200)