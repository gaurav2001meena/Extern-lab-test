# Generated by Django 4.1.7 on 2023-03-13 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='email',
        ),
    ]
