# Generated by Django 3.0.4 on 2020-04-24 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200420_2112'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='AskTagEndYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_bound', models.IntegerField(blank=True, null=True)),
                ('upper_bound', models.IntegerField(blank=True, null=True)),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskTagHomeCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_country_origin', to='accounts.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskTagMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ask_school', to='accounts.Major')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskTagSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ask_school', to='accounts.School')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskTagStartYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_bound', models.IntegerField(blank=True, null=True)),
                ('upper_bound', models.IntegerField(blank=True, null=True)),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskTagStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(choices=[('FU', 'Future Student'), ('CU', 'Current Student'), ('AL', 'Alumni')], default='CU', max_length=20)),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskTagStudyAbroadCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Ask')),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ask_country_study_abroad', to='accounts.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]