# Generated by Django 3.2.5 on 2021-11-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musics',
            name='cluster_a',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='musics',
            name='cluster_bl',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='musics',
            name='cluster_bs',
            field=models.IntegerField(null=True),
        ),
    ]