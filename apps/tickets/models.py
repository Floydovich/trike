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
        CLOSED = 'CLOSED'

        @classmethod
        def get_next(cls, status):
            try:
                return cls.values[cls.values.index(status) + 1]
            except IndexError:
                return cls.PENDING

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )

    @property
    def next_status(self):
        return Ticket.Status.get_next(self.status)
