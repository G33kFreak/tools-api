# Generated by Django 4.2.3 on 2023-07-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_date_end_booking_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_start',
            field=models.DateField(),
        ),
    ]