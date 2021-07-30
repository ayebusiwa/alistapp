from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import *
from product.models import *
from user.models import UserProfile


# Create your views here.
def index(request):
    setting= Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    testi = Testimonial.objects.all()
    banner = Product.objects.get(banner=True)
    offer = Product.objects.get(offer=True)
    category = Category.objects.all()[:3]
    featured = Product.objects.filter(featured= True)
    latest = Product.objects.filter(latest= True)[:4]
    latest2 = Product.objects.filter(latest= True).order_by('-id')[:4]
    
    
    context={
        'setting':setting,
        'brands': brands,
        'testi': testi,
        'banner': banner,
        'offer': offer,
        'category': category,
        'featured': featured,
        'latest': latest,
        'latest2': latest2,
    }
    return render(request, 'index.html', context)
    

def about(request):
    setting = Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    category = Category.objects.all()

    context = { 'setting': setting,
                'brands': brands,
                'category': category,
    }            

    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team will reach you soon.")
            return redirect('/contact')


    setting = Setting.objects.get(pk=1)
    form = ContactForm
    brands = Brand.objects.all()
    category = Category.objects.all()
       
    context= { 'setting': setting,
                'form': form,
                'brands': brands,
                'category': category,                
    }

    return render(request, 'contact.html', context)

def category(request):
    setting= Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    offer = Product.objects.get(offer=True)
    category = Category.objects.order_by('-created_at').filter(status=True)
    paginator = Paginator(category,4)
    page= request.GET.get('page')
    paged_category = paginator.get_page(page)
    
    context= {
            'setting': setting,
            'brands': brands,
            'offer': offer,
            'category': paged_category,
    }

    return render(request, 'categories.html', context)

def product_list(request,id,slug):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata= Category.objects.get(pk=id)
    products = Product.objects.filter(category__id=id)
    # products2 = Product.objects.filter(category_id=id).order_by('-id')[:4]
    paginator = Paginator(products,2)
    page= request.GET.get('page')
    paged_products = paginator.get_page(page)
    

    context= {
                'setting': setting,
                'category': category,
                'catdata': catdata,
                'products': paged_products,
                # 'products2': products2,
    }

    return render(request, 'products.html', context)
    # return HttpResponse(products)



def prod_detail(request,id,slug):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)

    
    context= {
                'setting': setting,
                'category': category,
                'products': products,
                'product': product,
                'images': images,
    }

    return render(request, 'product-details.html', context)