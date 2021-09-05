from customer.models import Customer
from django.db import models
from django.contrib.auth.models import User
import uuid
import random
import os


class BillType(models.Model):
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def filePathName(instance,filename):
    path = 'static/Bill'
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(10, 99))
    filename = stringId + randInt + extension
    return os.path.join(path,filename)

class Bill(models.Model):
    type = models.ForeignKey(BillType,on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    attachment = models.FileField(upload_to = filePathName,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add= True)

