# Generated by Django 4.0.6 on 2022-09-23 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webparsinginspectorulpadurii', '0006_alter_istoricmetricubi_day_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='istoricmetricubi',
            name='date',
        ),
    ]
