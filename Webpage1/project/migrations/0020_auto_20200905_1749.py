# Generated by Django 3.1 on 2020-09-05 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20200905_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
    ]