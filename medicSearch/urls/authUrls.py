from django.urls import path  
from medicSearch.views.authView import login_patient_view, register_view, logout_view

urlpatterns = [
    path('login-patient/', login_patient_view, name='login_patient'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout')
]
