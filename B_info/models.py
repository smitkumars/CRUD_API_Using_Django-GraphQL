
from django.db import models

# Create your models here.

class Business(models.Model):
    
    B_name= models.CharField("Capture name", max_length=255, blank = True, null = True)
    Owner_info= models.CharField("Owner Info", max_length=255, blank = True, null = True)
    email= models.EmailField()
    phone= models.CharField(max_length=20, blank = True, null = True)
    address= models.TextField(blank=True, null=True)
    employee_size= models.PositiveIntegerField(blank=True,null=True)
   # createdAt= models.DateTimeField("Created At",auto_now_add=True)


    def __str__(self):
        return self.B_name