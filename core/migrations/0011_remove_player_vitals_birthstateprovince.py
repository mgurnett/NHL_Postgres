# Generated by Django 4.2.2 on 2023-06-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_player_vitals_birthstateprovince'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player_vitals',
            name='birthStateProvince',
        ),
    ]
