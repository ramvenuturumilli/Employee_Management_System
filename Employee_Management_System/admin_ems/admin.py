from django.contrib import admin
from .models import user_auth,user_table
# Register your models here.

admin.site.register(user_table)
admin.site.register(user_auth)
