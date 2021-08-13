from django.contrib import admin

# Register your models here.
import Shop.models as model

admin.site.register(model.Product)
