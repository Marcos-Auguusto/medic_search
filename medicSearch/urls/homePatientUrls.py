from django.urls import path
from medicSearch.views.homePatientView import home_patient

urlpatterns = [
    path('home-patient', home_patient, name='home_patient'),

]
