# Generated by Django 4.1.5 on 2023-01-16 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0002_city_dayweek_speciality_state_profile_favorites_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.AddField(
            model_name='city',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='State', to='medicSearch.state'),
        ),
    ]
