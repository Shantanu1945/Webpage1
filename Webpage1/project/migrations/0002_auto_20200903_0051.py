# Generated by Django 3.1 on 2020-09-02 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productman',
            old_name='name2',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='websubcategory',
            old_name='name3',
            new_name='subcateg',
        ),
        migrations.RemoveField(
            model_name='inherit1',
            name='name1',
        ),
    ]