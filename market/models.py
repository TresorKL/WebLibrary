from tokenize import blank_re
from turtle import title
import uuid
from django.db import models

class Books(models.Model):
    author=models.CharField(max_length=50,null=True)
    title =models.CharField(max_length=50,null=True)
    price =models.IntegerField()
    type = models.CharField(max_length=50,null=True)
    id=models.UUIDField(editable=False, primary_key=True,unique=True,default=uuid.uuid4)
    
    def __str__(self):
        return self.title
    

    
