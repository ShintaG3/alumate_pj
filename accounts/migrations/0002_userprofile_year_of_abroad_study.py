# Generated by Django 2.2.3 on 2020-02-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='year_of_abroad_study',
            field=models.DateField(blank=True, null=True),
        ),
    ]
