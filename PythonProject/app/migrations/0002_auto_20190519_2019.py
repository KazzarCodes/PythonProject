# Generated by Django 2.2.1 on 2019-05-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contactNumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='contactPerson',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectStatus',
            field=models.CharField(max_length=100),
        ),
    ]
