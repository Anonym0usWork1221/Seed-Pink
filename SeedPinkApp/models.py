from django.db.models import CharField
from tinymce.models import HTMLField
from django.db import models
from datetime import datetime


class Posts(models.Model):
    slug = models.SlugField(null=False, editable=True, unique=True, default='')
    user_name = models.CharField(max_length=100, default="Abdul Moez")
    catagory = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    title_picture = models.ImageField(upload_to="title_images")
    title_picture_alt = models.CharField(max_length=30, default='')
    short_description = models.CharField(default='', max_length=1000)
    write_blog = HTMLField(default='')
    tags = models.CharField(default="", max_length=200)
    
    def __str__(self) -> CharField:
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #         super(Posts, self).save(*args, **kwargs)
        

class Portfolio(models.Model):
    slug = models.SlugField(null=False, editable=True, unique=True, default='')
    
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    company_link = models.URLField()
    
    title_picture = models.ImageField(upload_to="portfolio_images", null=False)
    title_picture_alt = models.CharField(max_length=30, default='', null=False)
    
    short_description = models.TextField(default='')
    blog_description = HTMLField(default='')
    
    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #         super(Portfolio, self).save(*args, **kwargs)
        
