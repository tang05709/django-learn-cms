from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.article, name='article'),
    path('article', views.article, name='article'),
    path('products', views.product, name='product'),
    path('product', views.product, name='product'),
    path('feedback', views.feedback, name='feedback'),
    path('posts', views.posts, name='posts'),
]