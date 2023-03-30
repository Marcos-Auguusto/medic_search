from django.urls import path
from medicSearch.views.homeView import home_view

urlpatterns = [
    path('', home_view),
    
]