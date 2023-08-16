from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicSearch.urls.homeUrls')),
    path('', include('medicSearch.urls.authUrls')),
    path('profile/', include('medicSearch.urls.profileUrls')),
    path('medic/', include('medicSearch.urls.medicUrls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


