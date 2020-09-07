from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactForm, ContactMessage
from product.models import Product, Images, Category
from django.contrib import messages
from home.forms import SearchForm
import json
from product.models import Comment

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4]#first 4
    products_deals = Product.objects.all().order_by('?')[:4]#experiment(dont know)
    products_latest = Product.objects.all().order_by('-id')[:4]#last 4
    products_picked = Product.objects.all().order_by('?')[:4]#random
    page = 'home'
    context = {'setting' : setting,
                'page' : page,
                'category' : category,
                'products_slider' : products_slider,
                'products_deals' : products_deals,
                'products_latest' : products_latest,
                'products_picked' : products_picked,
            }

    return render(request, 'home/index.html', context)
    #return HttpResponse('index page')

def aboutus(request): 
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'category' : category,
                'setting' : setting,
                }
    return render(request, 'home/about.html', context)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your message has been sent. Thank You!')
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context = {'setting' : setting, 'form' : form, 'category' : category }
    return render(request, 'home/contactus.html', context)
    #return HttpResponse('contact us')

def category_products(request, id, slug):
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'category' : category,
                'products' : products,
                'catdata' : catdata,
                }
    return render(request, 'home/category_products.html', context)

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products = Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'home/search_products.html', context)

    return HttpResponseRedirect('/')


def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for rs in products:
      products_json = {}
      products_json = rs.title
      results.append(products_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id = id)
    comments = Comment.objects.filter(product_id = id, status='True')
    context = {'category' : category,
                'product' : product,
                'images' : images,
                'comments' : comments,
                  }
    return render(request, 'home/product_detail.html', context)