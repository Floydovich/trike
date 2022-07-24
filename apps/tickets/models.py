from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
