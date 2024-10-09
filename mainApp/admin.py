from django.contrib import admin
from .models import Cars,Bikes,Mobiles,Applications

# Register your models here.

admin.site.register(Cars)
admin.site.register(Bikes)
admin.site.register(Mobiles)
admin.site.register(Applications)