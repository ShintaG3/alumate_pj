# Generated by Django 3.0.4 on 2020-04-24 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0002_auto_20200424_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ask',
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='AskLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='feed.Ask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AskCommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='feed.AskComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='askcomment',
            name='ask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feed.Ask'),
        ),
        migrations.AddField(
            model_name='askcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]