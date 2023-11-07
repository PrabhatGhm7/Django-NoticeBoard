from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from . import models

# Register your models here.

admin.site.register(models.Notice)



    


