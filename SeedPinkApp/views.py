from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Posts, Portfolio
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from random import shuffle
from slugify import slugify
import urllib.parse
import json
import os


def index(request):
    posts = Posts.objects.all()
    new_suggestions_list = [x for x in list(posts)]
    shuffle(new_suggestions_list)

    catagory = []
    for post in posts:
        if post.catagory not in catagory:
            catagory.append(post.catagory)

    context = {
        'post_suggestion': new_suggestions_list[:6],
        'posts_object': posts.order_by('-date')[0:3],
        'catagory': catagory
    }

    return render(request, "index.html", context)


def blog(request):
    posts = Posts.objects.all()
    catagory = []
    for post in posts:
        if post.catagory not in catagory:
            catagory.append(post.catagory)

    context = {
        'posts': posts,
        'posts_object': posts.order_by('-date')[0:3],
        'catagory': catagory
    }

    return render(request, "blog.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        sendable_message = """
            Message From Seed Pink Contact Form
            
            Sender_Name = {}
            Sender_Email = {}
            Sender_Message = {}
        """.format(data['name'], data['email'], data['message'])
        send_mail(data['subject'], sendable_message, '', ['seedpink1@gmail.com'])

        messages.info(request, "Message Sent")

        return redirect('contact')
    return render(request, "contact.html")


def posts(request, slug):
    instance = get_object_or_404(Posts, slug=slug)
    description = instance.write_blog

    context = {
        "post_details": instance,
        'description': description,
    }
    return render(request, "post-details.html", context)


def about(request):
    return render(request, "about.html")


def portfolio(request):
    portfolio_objects = Portfolio.objects.all()
    context = {
        'portfolio': portfolio_objects,
    }
    return render(request, "portfolio.html", context)


def catagory(request):
    catagory_id = request.GET.get('catagory_id')
    posts = Posts.objects.all()
    posts_catagory = Posts.objects.filter(catagory=catagory_id)

    catagory = []
    for post in posts:
        if post.catagory not in catagory:
            catagory.append(post.catagory)

    context = {
        'posts': posts.order_by('-date')[0:3],
        'posts_catagory': posts_catagory,
        'catagory': catagory,
        'catagory_id': catagory_id

    }

    return render(request, "catagory.html", context)


def policy(request):
    return render(request, "policy.html")


def tags(request):
    tag_id = request.GET.get('tag_id')
    posts = Posts.objects.all()
    tagged_posts = [x for x in posts if tag_id in x.tags]

    catagory = []
    for post in posts:
        if post.catagory not in catagory:
            catagory.append(post.catagory)

    context = {
        'posts': posts.order_by('-date')[0:3],
        'tagged_posts': tagged_posts,
        'catagory': catagory,
        'tag_id': tag_id

    }

    return render(request, 'tags.html', context)


def portfolio_samples(request, slug):
    instance = get_object_or_404(Portfolio, slug=slug)
    description = instance.blog_description

    context = {
        "post_details": instance,
        'description': description
    }

    return render(request, 'portfolio-samples.html', context)


@csrf_exempt
def upload_image(request):
    file = request.FILES['file']
    filenameParts = os.path.splitext(file.name)
    slugifiedFilename = slugify(filenameParts[0]) + filenameParts[1]
    osFilename = os.path.join(settings.MEDIA_ROOT, slugifiedFilename)
    with open(osFilename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    url = urllib.parse.urljoin(settings.MEDIA_URL, slugifiedFilename)
    data = json.dumps({"location": url})
    return HttpResponse(data, content_type='application/json')

