from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    image = models.ImageField(null=True ,blank=True , upload_to='uploads/pics')
    poster = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=30)
    contact_message = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

