# Generated by Django 3.2.5 on 2021-11-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioAPP', '0002_auto_20211117_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='fee_near_year',
            field=models.IntegerField(null=True),
        ),
    ]
