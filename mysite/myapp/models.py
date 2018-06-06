from django.db import models

# Create your models here.
class fasongzhe(models.Model):
    fname=models.CharField(max_length=20)
    fnumber=models.IntegerField()
    message=models.CharField(max_length=200)


class jieshouzhe(models.Model):
    jname=models.CharField(max_length=20)
    jnumber=models.IntegerField()
    jfasongzhe=models.ForeignKey(fasongzhe,on_delete=models.CASCADE)
