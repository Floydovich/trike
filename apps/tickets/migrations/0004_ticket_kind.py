# Generated by Django 4.0.6 on 2022-07-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='kind',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], default='', max_length=10),
        ),
    ]
