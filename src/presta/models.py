import datetime
from django.db import models
from django.utils import timezone
from datetime import datetime

TYPE_CHOICES = [
    ('FP', 'FP'),
    ('GS', 'Grande Soirée'),
    ('SC', 'Soirée Chill'),
    ('DM', 'Découverte Musicale'),
    ('AU', 'Autre')
]


class Presta(models.Model):
    presta_name = models.CharField('Nom de presta', max_length=200)
    presta_type = models.CharField(
        'Type de Presta désirée', max_length=3, choices=TYPE_CHOICES)
    presta_place = models.CharField(
        'Lieu de Presta', max_length=200, default='')
    presta_respo = models.CharField(
        'Personne responsable', max_length=200, default='')
    presta_respo_phone = models.CharField(
        'Numéro Respo', max_length=15, default='')
    presta_respo_mail = models.EmailField(
        'email respo', default='', blank=True)
    presta_date = models.DateField('date de presta', default=datetime.now)
    presta_start = models.TimeField('Heure de Début', default=datetime.now)
    presta_end = models.TimeField('Heure de Fin', default=datetime.now)
    presta_comments = models.TextField(
        'Commentaires Additionnels', default='', blank=True)
    pub_date = models.DateTimeField(
        'date published', default=datetime.now)

    def __str__(self):
        return self.presta_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
