# Generated by Django 3.1.6 on 2021-04-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presta', '0010_auto_20210417_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='presta',
            name='presta_respo_phone',
            field=models.CharField(default='', max_length=15, verbose_name='Numéro Respo'),
        ),
        migrations.AlterField(
            model_name='presta',
            name='presta_comments',
            field=models.TextField(blank=True, default='', verbose_name='Commentaires Additionnels (Genres Musicales souhaitées, Lien de Playlist, etc.)'),
        ),
        migrations.AlterField(
            model_name='presta',
            name='presta_respo_mail',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='email respo'),
        ),
    ]
