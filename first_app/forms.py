from turtle import width
from urllib import request
from django import forms
from django.core import validators
from first_app.models import Blog , Contact , Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class RegForm(UserCreationForm):
    GENDER_CHOICES=[
      ('male', 'MALE'),
      ('female', 'FEMALE')
    ]
  
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']



class Blogform(forms.ModelForm):
    class Meta():
        model = Blog
        fields =('name', 'email', 'title', 'body')

class CommentForm(forms.ModelForm):
    name = forms.CharField(label='name :', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name' ,'style':'width:200px;'}))
    email = forms.CharField(label='email :', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email' ,'style':'width:200px;'}))
    body = forms.CharField(label='content :',widget=forms.TextInput(attrs={'class': 'form-control', 'style':'width:800px;height:200px; '}))
    
    
    class Meta:
        model = Comment
        exclude = ['created_on','post']

class Contactform(forms.ModelForm):
    contact_name = forms.CharField(label='name :', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name','style':'width:200px;' }))
    contact_email = forms.EmailField(label='Email :',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    contact_subject = forms.CharField(label='subject :', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    contact_message = forms.CharField(label='message :', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message','style':'height:150px;'}))

    class Meta():
        model = Contact
        fields ='__all__'

