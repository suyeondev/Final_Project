# Generated by Django 3.2.5 on 2021-11-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('composer', models.CharField(max_length=50)),
                ('fee_near_year', models.IntegerField()),
                ('img_url_txt', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('img_url', models.ImageField(default='None.jpg', upload_to='static/img/title_img')),
            ],
        ),
    ]