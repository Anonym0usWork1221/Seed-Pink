# Generated by Django 4.1.7 on 2023-03-24 10:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('SeedPinkApp', '0005_alter_posts_title_picture_alt_alter_posts_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='description_file',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='blog_description',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]