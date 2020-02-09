from django.db import models

class Ask(models.Model):
    query_id=models.AutoField
    query=models.CharField(max_length=100)
    query_ans=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
