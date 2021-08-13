from django.contrib import admin

# Register your models here.
import Blog.models as model

admin.site.register(model.Blog)
