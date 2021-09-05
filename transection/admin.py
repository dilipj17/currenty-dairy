from django.views.generic.base import View
from transection.models import Transection 
from django.contrib import admin
from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

class TransectionAdminView(admin.ModelAdmin):
    change_list_template = "transection_changelist.html"
    list_display = ['transection_id','timestamp','date','remarks','customer','credit','amount','balance_amount']
    search_fields = ['customer__name','customer__code']
    autocomplete_fields = ['customer']
    readonly_fields = ['balance_amount']
    list_per_page=50  

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Transection,TransectionAdminView)
