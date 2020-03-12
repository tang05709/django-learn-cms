from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'data': 'test'
    }
    return render(request, 'index.html', context)

def articles(request):
    context = {
        'data': 'test'
    }
    return render(request, 'articles.html', context)

def article(request):
    context = {
        'data': 'test'
    }
    return render(request, 'article.html', context)

def products(request):
    context = {
        'data': 'test'
    }
    return render(request, 'products.html', context)

def product(request):
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
    context = {
        'data': 'test'
    }
    return render(request, 'posts.html', context)