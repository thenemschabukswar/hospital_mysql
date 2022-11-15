from django.contrib import admin
from .models import patient
from .models import hosp
# from .models import rooms
# Register your models here.
admin.site.register(patient)
admin.site.register(hosp)