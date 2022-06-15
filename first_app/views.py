from django.shortcuts import render,redirect
from first_app.forms import Blogform ,RegForm, CommentForm, Contactform
from django.views.generic import ListView , DetailView
from first_app.models import Blog,Comment,Contact,Services
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.

def index(request):
  return render (request,'first_app/index.html')


def blog(request):
  return render (request,'first_app/blog.html')

def base(request):
  return render (request,'first_app/base.html')


def about(request):
  return render (request,'first_app/about.html')

def portfolio(request):
  return render (request,'first_app/portfolio.html')



def services(request):
  return render (request,'first_app/services.html')

def register(request):
  if request.method == 'POST':
    register_form = RegForm(request.POST)
    if register_form.is_valid():
        register_form.save()
        return redirect('backend:login')
  else:
    register_form = RegForm()
  return render(request, 'first_app/register.html', {'reg':register_form})

@login_required
def contact(request):
  if request.method == 'POST':
    contact_form = Contactform(request.POST)
    if contact_form.is_valid():
        contact_form.save()
        contact_form = Contactform()
  else:
    contact_form = Contactform()
  return render(request, 'first_app/contact.html', {'cont':contact_form})
  
def blogform(request):
  blog = Blog.objects.all()
  return render (request,'first_app/blog.html', {'blog':blog} )

def contactform(request):
  contact = Contact.objects.all()
  return render (request,'first_app/blog.html', {'contact':contact} )


class ListBlog(ListView):
  model = Blog
  template_name = 'first_app/list.html'
  context_object_name ='list_blog'

class Serve(ListView):
  model = Services
  template_name = 'first_app/services.html'
  context_object_name ='list_services'

def secondblog(request, pk):
    detail_post = get_object_or_404(Blog, pk=pk)
    comm = Comment.objects.filter(post=pk).order_by('-created_on')
    most_recent = Blog.objects.order_by('-created_on')[:3]
    # Comment posted
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post = detail_post
           comment.save()
           return redirect('secondblog',pk=detail_post.pk )
         
    else:
      form = CommentForm()
      return render(request,'first_app/single-blog.html', {'comm':comm, 'form':form,'most_recent':most_recent,  'blog_detail':detail_post})