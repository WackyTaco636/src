from django.contrib import admin

# Register your models here.
# CW the import below is known as a relative import because both files are in the same directory (i.e. same module)
from .models import Product

admin.site.register(Product)
