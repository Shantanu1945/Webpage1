# Generated by Django 3.1 on 2020-09-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200903_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Category name'),
        ),
    ]
