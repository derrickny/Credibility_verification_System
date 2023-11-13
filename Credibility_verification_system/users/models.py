from django.contrib.auth.models import AbstractUser
from django.db import models
from .fields import PercentField
from django_countries.fields import CountryField


    


GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    # You can add more options here
]

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = CountryField(blank=True,default='') 
    gender = models.CharField(max_length=6, choices= GENDER_CHOICES, default='', blank=True)
    username = models.CharField(unique=True,max_length=255,default="")
    email = models.EmailField(unique=True, default="")
    password = models.CharField(max_length=255)
    retype_password = models.CharField(max_length=255)
    otp = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.username 


class Statement(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    statement = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    statement_id = models.ForeignKey(Statement, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
class Verdict(models.Model):
    id = models.AutoField(primary_key=True)
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
    statement_id = models.ForeignKey(Statement, on_delete=models.CASCADE)
    Statement_verdict = models.CharField(max_length=255,default="")
    predicted_probability = PercentField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.Statement_verdict  
    
    
class StatementVerdict(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    verdict = models.ForeignKey(Verdict, on_delete=models.CASCADE)
    
    
    
    
