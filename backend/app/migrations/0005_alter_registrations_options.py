# Generated by Django 4.2.3 on 2024-07-11 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_waitlist_registrations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrations',
            options={'verbose_name': 'Wailist Registration', 'verbose_name_plural': 'Waitlist Registrations'},
        ),
    ]
