# Generated by Django 3.1 on 2020-09-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200903_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(default=3, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Category name'),
        ),
    ]
