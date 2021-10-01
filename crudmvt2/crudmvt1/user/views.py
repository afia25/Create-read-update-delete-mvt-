from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import *
#from . import loaddata
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *



def register(request):
    if (request.method=="POST"):
        form=UserRegistrationForm(request.POST)
        #profileform = RegistrationProfileForm(request.POST)
        #if (form.is_valid() and profileform.is_valid()):
        if (form.is_valid()):
            #error=''
            #dict=request.POST
            #username=dict['username']
            #check=User.objects.filter(username='username')
            #if len(check)==0:
            form.save()
            #profileform.save()

            #else:
                #error='Username already exists.'
                #return render(request, 'customer/register.html', {'form':form,'error':error})

            user = get_user(request)

            uname=form.cleaned_data.get('username')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            psw = form.cleaned_data.get('password1')
            c = User.objects.get(username__exact=uname)
            c.first_name = fname
            c.last_name = lname
            c.email = email
            c.save()

            new_user=authenticate(username=uname,password=psw)
            login(request,new_user)

            # shows msg in home after registration
            #message='Welcome to Inventory Management System'
            #messages.success(request, message=message)
            return redirect('addproduct')


        else:
            context={
                'form':form
            }
            return render(request, 'user/register.html', context)

    else:
        form = UserRegistrationForm()
        #profileform=RegistrationProfileForm()
        #return render(request, 'customer/register.html', {'form':form,'profileform':profileform})
        return render(request, 'user/register.html', {'form': form})


@login_required
def home(request):
    user = get_user(request)
    context = {
        'name': user.username,

    }
    #shows msg in home after login
    #message = 'Welcome to Inventory Management System'
    #messages.success(request, message=message)
    return render(request,'user/home.html', context)


def base(request):
    return render(request,'user/base.html')

def user(request):
    return render(request,'user/home.html')





