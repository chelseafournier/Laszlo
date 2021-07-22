from django.db import models

# Create your models here.
class ContactMe(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=191)