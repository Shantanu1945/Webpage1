# Generated by Django 3.1 on 2020-09-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_inherit1_x'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inherit1',
            name='x',
            field=models.CharField(max_length=50, null=True),
        ),
    ]