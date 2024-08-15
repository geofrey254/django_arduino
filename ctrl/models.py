from django.db import models

# Create your models here.


class Serial(models.Model):
    is_on = models.BooleanField(default=False)
