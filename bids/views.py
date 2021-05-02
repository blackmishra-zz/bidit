from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    products = Product.objects
    return render(request, 'bids/home.html', {'products':products})

@login_required(login_url="/accounts/login")
def create(request):
    if request.method=='POST':
        if (request.POST['title'] and request.POST['body'] and request.POST['category'] and request.POST['price'] and request.FILES['icon'] and request.FILES['image']):
            product = Product()
            product.title = request.POST['title']
            product.category = request.POST['category']
            product.price = request.POST['price']
            product.body = request.POST['body']            
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.seller = request.user
            product.save()
            return redirect('/bids/' + str(product.id))

        else:return render(request, 'bids/create.html', {'error':'All fields are mandatory'})

    else:return render(request, 'bids/create.html')


@login_required(login_url="/accounts/login")
def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'bids/details.html', {'product':product})

def cart(request):
    return render(request, 'bids/cart.html')
    
def category(request):
    products = Product.objects
    return render(request, 'bids/category.html', {'products':products})

def contact(request):   
    return render(request, 'bids/contact.html')

def about(request):
    return render(request, 'bids/about.html')

def send_mess(request):
    email_to = 'rockdtaz@gmail.com'
    sub = request.POST.get('subject')
    mes = request.POST.get('message')
    sender_email = request.POST.get('email')
    body = (sub, mes, sender_email, email_to)
    res = send_mail(sub,mes,sender_email,[email_to],fail_silently=False,)
    if res == 1: 
        messages.info(request, 'Mail sent successfully!')
        return render(request, 'bids/contact.html')
    else:render(request, '/about.html', {'mess':'Something went wrong. Please try again..'})