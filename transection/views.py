from customer.models import Customer
from transection.models import Transection
from django.forms import forms
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from django.views.generic import FormView
import pandas as pd
from django.contrib import messages
from .admin import SuperUserCheck

class MassUploadTransectionForm(forms.Form):
	choose_file = forms.FileField()


class MassUploadTransections(SuperUserCheck,FormView):
    form_class = MassUploadTransectionForm
    template_name = 'massuploadtransection.html'

    def form_valid(self,form):
        request = self.request
        row_processed = 0
        if self.request.method == 'POST':
            file = form.cleaned_data['choose_file']
            try:
                df = pd.read_excel(file)
                for i,row in df.iterrows():
                    customer = Customer.objects.get(code = row['customer'])
                    Transection.objects.create(
                        date = row['date'],
                        transection_id = row['id'],
                        customer = customer,
                        credit = row['credit'],
                        amount = row['amount'],
                        remarks = row['remarks']
                    )
                    row_processed+=1
            except Exception as e:
                messages.error(request,'Row Processed  {} Error: {} in Row Number {}'.format(row_processed,e,row_processed+2))
                return redirect(request.META['HTTP_REFERER'])
            messages.success(request,'All Data has succesfully processed and update to database')
            return redirect(self.request.META['HTTP_REFERER'])