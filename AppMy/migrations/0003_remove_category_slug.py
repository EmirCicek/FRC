# Generated by Django 4.2.15 on 2024-08-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMy', '0002_card_category_delete_project_card_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
