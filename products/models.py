from django.db import models

# Create your models here.
# CW: Get the class to inherit from the default classe of model and use models to incorporate the standard text fields.
class Product(models.Model) :
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='this is cool!')
