# Generated by Django 4.1.7 on 2023-03-24 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=100)),
                ('company_link', models.URLField()),
                ('title_picture', models.ImageField(upload_to='portfolio_images')),
                ('short_description', models.TextField(default='')),
                ('description_file', models.FileField(upload_to='portfolio_samples')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('user_name', models.CharField(default='Admin', max_length=100)),
                ('catagory', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('title_picture', models.ImageField(upload_to='title_images')),
                ('short_description', models.TextField(default='')),
                ('description_file', models.FileField(upload_to='description_files')),
                ('tags', models.TextField(default='')),
            ],
        ),
    ]