from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'addresses',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(state)
admin.site.register(address)
admin.site.register(neighborhood)
admin.site.register(dayWeek)
admin.site.register(rating)
admin.site.register(speciality)
admin.site.register(city)




