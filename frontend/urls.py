from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:cid>', views.articles, name='article'),
    path('detail/<int:id>', views.article, name='article'),
    path('products/<int:cid>', views.products, name='product'),
    path('product/<int:id>', views.product, name='product'),
    path('feedback', views.feedback, name='feedback'),
    path('about', views.posts, name='posts'),
    path('curture', views.posts, name='posts'),
]