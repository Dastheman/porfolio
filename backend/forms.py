from dataclasses import field, fields
import email
from email.mime import image
from pyexpat import model
from tkinter.ttk import Style
from turtle import title
from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from first_app.models import*

# class Blog(forms.Form):
    
#   name = forms.CharField()
#   subject = forms.CharField(help_text='Make sure you include just in title')
#   email = forms.EmailField()
#   vemail = forms.EmailField(label='Enter your email again')
#   text = forms.CharField(widget=forms.Textarea, required=False)
#   botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
#                               validators.MaxLengthValidator(0)])
#   def clean(self):
#       cleaned_data = super().clean()
#       email = cleaned_data.get('email')
#       vmail = cleaned_data.get('vemail')
#       if email != vmail:
#           raise forms.ValidationError('Your first email and second email must match')


#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)

# class FormName3(forms.Form):

#   name = forms.CharField()
#   subject = forms.CharField(help_text='Make sure you include just in title')
#   email = forms.EmailField()
#   vemail = forms.EmailField(label='Enter your email again')
#   text = forms.CharField(widget=forms.Textarea, required=False)
#   botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
#                               validators.MaxLengthValidator(0)])

class AddBlogForm(forms.ModelForm):
  title = forms.CharField(label='Title :', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your title',}))
  image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control','placeholder':'Upload your picture',}))
  body = forms.CharField(label='Content :', widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter content', 'style':"width: 100%; height: 150px"}))
  

  class Meta():
    model = Blog
    fields = ['title','image','body', 'poster']


class EditProfileForm(forms.ModelForm):
  username = forms.CharField(label='Username :', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter username',}))
  first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter firstname',}))
  last_name = forms.CharField(label='Last name :', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter lastname',}))
  email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email',}))

  def clean_email(self):
      email_field = self.cleaned_data.get('email')
      if User.objects.filter(email=email_field).exists():
          raise forms.ValidationError('Email alreadly exist')
      return email_field

  class Meta():
    model = User
    fields = ['username','first_name','last_name','email']


class ChangePasswordForm(PasswordChangeForm):
  old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password','style':'width:40%'}))
  new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password','style':'width:40%'}))
  new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password','style':'width:40%'}))

  class Meta():
      model = User
      fields = ['old_password','new_password1','new_password2']

class EditBlogForm(forms.ModelForm):
  class Meta():
    model = Blog
    exclude = ['User']