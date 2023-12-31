# Generated by Django 4.2.3 on 2023-07-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='tools')),
                ('available_count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
    ]
