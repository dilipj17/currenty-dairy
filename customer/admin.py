from django.contrib import admin
from .models import Customer

class CustomerAdminView(admin.ModelAdmin):
    list_display = ('code','name','guardian_name','village','contact_no','timestamp')
    search_fields = ('code','name','guardian_name')

admin.site.register(Customer,CustomerAdminView)