# Generated by Django 4.1.7 on 2023-03-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeedPinkApp', '0002_remove_posts_description_file_posts_write_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
