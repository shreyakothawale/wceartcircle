# Generated by Django 3.1.6 on 2021-03-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('board', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('insta', models.URLField(blank=True)),
                ('artwork', models.CharField(blank=True, max_length=100)),
                ('artworklink', models.URLField(blank=True)),
                ('valid', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]