# Generated by Django 4.2.4 on 2023-08-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about_booking_alter_doctors_dep_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='dep_name',
            field=models.CharField(max_length=100),
        ),
    ]