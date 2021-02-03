from django.db import models


class Objects(models.Model):
    value = models.CharField(max_length=250)
    nds = models.BooleanField(blank=True, default=False)
    nds_value = models.IntegerField(blank=True, default=20)
