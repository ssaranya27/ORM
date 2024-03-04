from django.contrib import admin

# Register your models here.
from .models import Bookdetails,BookdetailsAdmin
admin.site.register(Bookdetails,BookdetailsAdmin)