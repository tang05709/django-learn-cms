from django.shortcuts import render
from common.models import Article, Category

# Create your views here.
def index(request):
    context = {
        'data': 'test'
    }
    return render(request, 'index.html', context)

def articles(request, cid):
    articles = Article.objects.filter(category_id = cid)

    context = {
        'articles': articles
    }
    return render(request, 'articles.html', context)

def article(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'article.html', context)

def products(request, cid):
    context = {
        'data': 'test'
    }
    return render(request, 'products.html', context)

def product(request, id):
    context = {
        'data': 'test'
    }
    return render(request, 'product.html', context)

def feedback(request):
    context = {
        'data': 'test'
    }
    return render(request, 'feedback.html', context)

def posts(request):
    seo_path = (request.path).replace('/frontend/', '', 1)
    content = ''
    if seo_path is not None:
        posts = Category.objects.get(seo_path=seo_path)
        if posts is not None:
            content = posts.content

    context = {
        'content': content
    }
    return render(request, 'posts.html', context)