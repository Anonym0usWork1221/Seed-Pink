from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('post-details/<slug:slug>',views.posts,name="post-details"),  # changed
    path('about', views.about, name="about"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('catagory', views.catagory, name="catagory"),
    path('privacy-policy', views.policy, name="privacy-policy"),
    path('tags', views.tags, name="tags"),
    path('portfolio-samples/<slug:slug>', views.portfolio_samples, name="portfolio-samples"),
    path("upload-file", views.upload_image, name="upload_image"),
]
