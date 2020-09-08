# Generated by Django 3.1 on 2020-09-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, null=True, unique=True, verbose_name='Category name')),
                ('id', models.AutoField(default=3, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ProductMan',
            fields=[
                ('name2', models.CharField(max_length=50, null=True)),
                ('ProductMan_id', models.AutoField(default=1, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'ProductMan',
            },
        ),
        migrations.CreateModel(
            name='WebSubCategory',
            fields=[
                ('name3', models.CharField(max_length=50, null=True)),
                ('WebSubcategory_id', models.AutoField(default=2, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='project.category', verbose_name='Select category')),
            ],
            options={
                'verbose_name_plural': 'WebSubCategory',
            },
        ),
        migrations.CreateModel(
            name='Inherit1',
            fields=[
                ('productman_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='project.productman')),
                ('websubcategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='project.websubcategory')),
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='project.category')),
                ('name1', models.CharField(max_length=50, null=True)),
            ],
            bases=('project.category', 'project.websubcategory', 'project.productman', models.Model),
        ),
        migrations.AddField(
            model_name='productman',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productsman', to='project.websubcategory', verbose_name='Select subcategory'),
        ),
    ]