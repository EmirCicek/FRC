# Generated by Django 4.2.15 on 2024-10-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMy', '0005_sponsorcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_live',
            field=models.BooleanField(default=False),
        ),
    ]
