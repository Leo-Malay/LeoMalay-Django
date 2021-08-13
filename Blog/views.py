from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Blog.models import Blog


def index(request):
    return render(request, "blog/home.html", {'title': "Blogs", 'blog_list': [{'title': 'How I made it to Google', 'date': '29-May-2025', 'img': '/IMG/Test_blog.jfif'}, {'title': 'Fortune 500 really worth it?', 'date': '29-May-2025', 'img': '/IMG/Test_blog.jfif'}]})


def article(request):
    try:
        a_id = request.GET['id']
    except:
        a_id = False
    if a_id:
        try:
            data = list(Blog.objects.filter(id=a_id).values())
            return render(request, "blog/article.html", {'title': "Article", 'data': {'title': data[0]['title'], 'author': data[0]['author'], 'image': data[0]['image'], 'content': data[0]['content']}})
        except:
            return index(request)
    return index(request)
