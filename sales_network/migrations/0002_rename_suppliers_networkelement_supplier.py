# Generated by Django 5.0 on 2023-12-27 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_network', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkelement',
            old_name='suppliers',
            new_name='supplier',
        ),
    ]
