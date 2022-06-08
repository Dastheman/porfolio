from django.contrib import admin
from first_app.models import Blog,Contact,Comment
# Register your models here.



admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Contact)


