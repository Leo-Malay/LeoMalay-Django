from django.contrib import admin

# Register your models here.
import Auth.models as model

admin.site.register(model.Account)
