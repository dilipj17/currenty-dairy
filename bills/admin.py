from bills.models import Bill
from django.contrib import admin
from django.utils.html import mark_safe

class BillAdminView(admin.ModelAdmin):
    list_display = ['type','customer','date','amount','attachment']
    list_filter = ['type','customer']


admin.site.register(Bill,BillAdminView)