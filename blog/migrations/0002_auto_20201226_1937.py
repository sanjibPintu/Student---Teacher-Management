# Generated by Django 3.0.9 on 2020-12-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='EmployeeNo',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phoneNo',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]