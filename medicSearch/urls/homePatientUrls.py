from django.urls import path
from medicSearch.views.homePatientView import home_view

urlpatterns = [
    path('', home_view),
    
]