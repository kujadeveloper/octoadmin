from django.db import models

class OctoModel(models.Model):
    class Meta:
        ordering = ['id']
        db_table = 'octo'

    Hostname = models.CharField(max_length=300)
    Ip = models.CharField(max_length=50)