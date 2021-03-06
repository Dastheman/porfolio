"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from ast import increment_lineno
from django.contrib import admin
from django.urls import path, include
from first_app import views
from django.conf.urls.static import static
from django.conf import settings
from first_app.models import Blog,Services
from django.contrib.auth import views as auth_views



urlpatterns = [
     
    path('', views.index, name='index'),
    path('blog/', views.blogform, name='blog'),
    path('base/', views.base, name='base'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('list_blog/', views.ListBlog.as_view(model=Blog), name='list_blog'),
    path('services/', views.Serve.as_view(model=Services), name='services'),
    # path('product_detail/<int:pk>', views.ProductDetail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('secondblog/<int:pk>', views.secondblog, name='secondblog'),
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls'))
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
