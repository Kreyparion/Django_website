import datetime
from django.db import models
from django.utils import timezone

TYPE_CHOICES = [
    ('FP', 'FP'),
    ('GS', 'Grande Soirée'),
    ('SC', 'Soirée Chill'),
]


class Presta(models.Model):
    presta_name = models.CharField(max_length=200)
    presta_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    presta_respo = models.CharField(max_length=200)
    presta_respo_mail = models.EmailField('email respo')
    presta_date = models.DateTimeField('date of presta')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.presta_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
