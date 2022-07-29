from django.db import models


class Ticket(models.Model):

    class Kind(models.TextChoices):
        BUG = 'Bug'
        FEATURE = 'Feature'

    kind = models.CharField(
        max_length=10,
        choices=Kind.choices,
        default='',
    )

    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    class Status(models.TextChoices):
        PENDING = 'PENDING'
        IN_REVIEW = 'IN REVIEW'
        DONE = 'DONE'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
