# Generated by Django 4.2.2 on 2023-06-13 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_team_abbreviation_alter_team_teamname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('nhl_id', models.IntegerField()),
                ('jerseyNumber', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('position_name', models.CharField(max_length=100)),
                ('position_type', models.CharField(max_length=100)),
                ('position_ab', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
            options={
                'ordering': ['jerseyNumber'],
            },
        ),
    ]
