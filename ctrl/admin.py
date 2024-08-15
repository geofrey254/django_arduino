from django.contrib import admin
from .models import Serial

# Register your models here.


class SerialAdmin(admin.ModelAdmin):
    list_display = ["is_on"]


admin.site.register(Serial, SerialAdmin)
