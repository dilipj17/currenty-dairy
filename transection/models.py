from django.db import models
from django.utils import timezone
from customer.models import Customer
from django.dispatch import receiver
from django.db.models.signals import pre_save,pre_delete

class Transection(models.Model):
    date = models.DateField(default=timezone.now,blank=True)
    transection_id = models.IntegerField(unique=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    credit = models.BooleanField(default=False)
    amount = models.IntegerField()
    balance_amount = models.IntegerField(null = True)
    remarks = models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.transection_id,self.customer.name,self.amount)


@receiver(pre_save,sender=Transection)
def addBalanceAmount(sender,**kwargs):
    obj = kwargs['instance']
    balance = 0
    diff = 0
    try:
        last_transection = Transection.objects.filter(customer = obj.customer).latest('timestamp')
        balance = last_transection.balance_amount
    except:
        balance = 0
    if(obj.credit == True):
        obj.balance_amount =  balance + obj.amount
    else:
        obj.balance_amount =  balance - obj.amount

@receiver(pre_delete,sender=Transection)
def deleteTransectionUpdateBalance(sender,**kwargs):
    obj = kwargs['instance']
    all_transections = Transection.objects.filter(timestamp__gte = obj.timestamp,customer = obj.customer).order_by('timestamp')
    prev = obj.balance_amount
    if(obj.credit):
        prev -= obj.amount
    else:
        prev += obj.amount
    for i in range(1,len(all_transections)):
        if(all_transections[i].credit):
            all_transections[i].balance_amount = prev + all_transections[i].amount
        else:
            all_transections[i].balance_amount = prev - all_transections[i].amount
        prev = all_transections[i].balance_amount
        Transection.objects.filter(pk = all_transections[i].id).update(balance_amount = prev)