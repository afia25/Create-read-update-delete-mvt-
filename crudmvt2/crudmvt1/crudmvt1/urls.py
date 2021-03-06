"""crudmvt1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user import views as views1
from product import views as pviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views1.register,name='register'),
    path('base/',views1.base),
    path('home/',views1.home,name='home'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('user/',views1.user,name='user'),


   path('addproduct/',pviews.addproduct,name='addproduct'),
   path('productlist/',pviews.productlist,name='productlist'),
   path('delete/',pviews.delete,name='delete'),

]