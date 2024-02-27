from django.urls import path
from medicSearch.views.profileView import list_profile_view, edit_profile

urlpatterns = [
    path('', list_profile_view, name='profiles'),
    path('<int:id>', list_profile_view, name='profile'),
    path('edit', edit_p rofile, name='edit_profile'),
        
]