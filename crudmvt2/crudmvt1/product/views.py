
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from django.contrib import messages


from .form import *


def addproduct(request):
    if (request.method=="POST"):
        addproductform = AddProductForm(request.POST)
        if (addproductform.is_valid()):
            addproductform.save()

           # views1.stock(request)
            return redirect('productlist')
        else:
            context = {
                'addproductform': addproductform,
            }
            return render(request, 'product/addproduct.html', context)
    else:
        addproductform = AddProductForm()
        context = {
            'addproductform': addproductform,
        }
        return render(request, 'product/addproduct.html', context)




def productlist(request):
    if (request.method=='POST'):
        dict=request.POST
        a=dict['id']
        obj=Product.objects.get(id__exact=a)

        b=dict['name']
        obj.product_name=b

        obj.category_name = dict['category']

        obj.description = dict['description']

        b = dict['bp']
        obj.buying_price =int(b)

        b = dict['sp']
        obj.selling_price = int(b)

        b = dict['purchase']
        obj.purchase = int(b)

        b = dict['sale']
        obj.sale = int(b)

        b = dict['stock']
        obj.stock = int(b)

        obj.save()

        products = Product.objects.all()
        return render(request,'product/productlist.html',{'products':products})

    else:
        products = Product.objects.all()
        return render(request, 'product/productlist.html', {'products': products})


def delete(request):
    if (request.method=='POST'):
        dict=request.POST
        a=dict['id']
        obj=Product.objects.get(id__exact=a)

        obj.delete()
        products=Product.objects.all()
        return render(request, 'product/delete.html', {'products': products})

    else:
        products = Product.objects.all()
        return render(request, 'product/delete.html', {'products': products})






