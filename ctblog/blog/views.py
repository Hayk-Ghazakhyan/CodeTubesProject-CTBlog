from django.shortcuts import render, HttpResponse
from django.http import request
from .models import Blog, Contact
from .forms import ContactForm
# Create your views here.

def home_page(request):
    context = {}
    blogs = Blog.objects.all()
    context["blogs"] = blogs
    return render(request, 'home.html', context)

def contact_us(request):
    context = {}
    if request.POST:
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        else:
            context["errors"] = my_form.errors

    return render(request, 'contact_us.html', context)

def blog_detail(request, pk):
    context= {}
    blog = Blog.objects.get(id = pk)
    context['blog'] = blog
    return render(request, 'blog_detail.html', context)

