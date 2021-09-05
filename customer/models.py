from django.db import models

class Customer(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length= 50)
    guardian_name = models.CharField(max_length= 50,null=True,blank=True)
    village = models.CharField(max_length= 25,null=True,blank=True)
    contact_no = models.IntegerField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.code)+" "+str(self.name)+" / "+str(self.guardian_name)
    
    class Meta:
        ordering = ['code']
