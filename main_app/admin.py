from django.contrib import admin
# import your models here
from .models import Car, ServicesCompleted

# Register your models here.
admin.site.register(Car)
admin.site.register(ServicesCompleted)