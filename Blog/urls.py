from django.urls import path
import Blog.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('article', views.article, name='article'),
]
