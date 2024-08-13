from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'addresses',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(Address)
admin.site.register(Neighborhood)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
admin.site.register(City)




