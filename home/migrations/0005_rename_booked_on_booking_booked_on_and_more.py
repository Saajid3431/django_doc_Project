# Generated by Django 4.2.4 on 2023-08-12 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_doctors_dep_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_on',
            new_name='Booked_on',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='Booking_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='doc_name',
            new_name='Doctor_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='p_email',
            new_name='Patient_email',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='p_name',
            new_name='Patient_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='p_phone',
            new_name='Patient_phone',
        ),
    ]