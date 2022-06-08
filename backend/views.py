from unicodedata import name
from django.shortcuts import render,redirect,get_object_or_404
from backend.forms import *
from backend.models import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash , login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/backend:login/')
def dashboard(request):
    return render(request, 'backend/index.html')

def backendblog(request):
    return render(request, 'backend/backblog.html')
def base(request):
  return render (request,'backend/base.html')


def blogform(request):
  if request.method == 'POST':
    blog_form = Blog(request.POST)
    if blog_form.is_valid():
        blog_form.save()
  else:
    blog_form = Blog()
  return render(request, 'backend/backblog.html', {'boo':blog_form})

def add_blog(request):
  if request.method == 'POST':
    blog = AddBlogForm(request.POST,request.FILES)
    if blog.is_valid():
      blog.save()
      blog = AddBlogForm()
  else:
    blog = AddBlogForm()
  return render(request, 'backend/add-blog.html',{'blog':blog,})

def view_blog(request):
  view_blog = Blog.objects.filter(poster=request.user)
  return render(request,'backend/view-blog.html',{'view':view_blog})

def edit_profile(request):
  if request.method == 'POST':
    edit_profile = EditProfileForm(request.POST,request.FILES)
    if edit_profile.is_valid():
      edit_profile.save()
      edit_profile.succes(request, 'Successful')
  else:
    edit_profile = EditProfileForm()
  return render(request, 'backend/edit_profile.html',{'edit_pro':edit_profile})

def Login_View(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('backend:dashboard')
    else:
      messages.error(request, "Username and Password do not match")
  return render(request,'backend/login.html')

def view_profile(request):
    return render(request, 'backend/view_profile.html',{'profile': request.user})

@login_required(login_url='/backend:login/')
def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('backend:login')

def passwordview(request):
  if request.method == 'POST':
    form = PasswordChangeForm(data=request.POST, user=request.user)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request,form.user)
      messages.success(request,'Password Changed Successfully')
  else:
    form = PasswordChangeForm(user=request.user)
  return render(request,'backend/changepassword.html', {'form_key':form})

def edit_post(request, pk):
  editblog = get_object_or_404(Blog, pk=pk)
  if request.method == 'POST':
    editblog = EditBlogForm(request.POST, request.FILES, instance=editblog)
    if editblog.is_valid():
      editblog.save()
      return redirect('backend:viewblog')
      messages.success(request, 'successful')
  else:
    editblog =EditBlogForm(instance=editblog)
  return render(request, 'backend/editpost.html' ,{'edit':editblog})


def view_post (request,pk):
  post = get_object_or_404(Blog, pk=pk)
  return render(request, 'backend/viewpost.html', {'post':post})
  return redirect('backend:viewblog')

def delete_post (request, pk):
  record = get_object_or_404(Blog, pk=pk)
  record.delete()
  return redirect('backend:viewblog')

