# Generated by Django 5.2 on 2025-05-11 04:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_rename_auther_notes_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='views_count',
        ),
        migrations.AddField(
            model_name='notes',
            name='views_count',
            field=models.ManyToManyField(related_name='Note', to=settings.AUTH_USER_MODEL),
        ),
    ]
