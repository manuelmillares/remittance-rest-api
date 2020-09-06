from django.contrib import admin
from apps.core import models


admin.site.register(models.User)
admin.site.register(models.Remittance)
