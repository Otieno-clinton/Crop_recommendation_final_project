from django.contrib import admin
from recommendapp.models import Contact, Farmer,GovernmentAgency, NGO

# Register your models here.
admin.site.register(Contact)
admin.site.register(Farmer)
admin.site.register(GovernmentAgency)
admin.site.register(NGO)