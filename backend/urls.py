from django.urls import path

from .views.AdvPositionView import AdvPositionIndexView, AdvPositionCreateView, AdvPositionUpdateView, AdvPositionDeleteView
from .views.AdvView import AdvIndexView, AdvCreateView, AdvUpdateView, AdvDeleteView
from .views.ConfigView import ConfigIndexView, ConfigCreateView, ConfigUpdateView, ConfigDeleteView
from .views.FeedbackView import FeedbackIndexView, FeedbackDetailView, FeedbackDeleteView
from .views.FriendLinkView import FriendLinkIndexView, FriendLinkCreateView, FriendLinkUpdateView, FriendLinkDeleteView
from .views.CategoryView import CategoryIndexView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from .views.PostsView import PostsIndexView, PostsCreateView, PostsUpdateView, PostsDeleteView
from .views.ArticleView import ArticleIndexView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from .views.ProductView import ProductIndexView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views.UploadFileView import UploadFileView
from .views.SiteView import LoginView, LoginInView, LoginOutView
from .views.TestView import TestView

app_name = 'backend'

urlpatterns = [
    path('test', TestView.as_view(), name = 'test'),
    path('upload', UploadFileView.as_view(), name = 'upload'),
    path('login', LoginView.as_view(), name = 'login'),
    path('login-in', LoginInView.as_view(), name = 'login-in'),
    path('login-out', LoginOutView.as_view(), name = 'login-out'),

    path('adv-position/index', AdvPositionIndexView.as_view(), name = 'adv-position-index'),
    path('adv-position/create', AdvPositionCreateView.as_view(), name = 'adv-position-create'),
    path('adv-position/update/<int:pk>', AdvPositionUpdateView.as_view(), name = 'adv-position-update'),
    path('adv-position/delete/<int:pk>', AdvPositionDeleteView.as_view(), name = 'adv-position-delete'),

    path('adv/index', AdvIndexView.as_view(), name = 'adv-index'),
    path('adv/create', AdvCreateView.as_view(), name = 'adv-create'),
    path('adv/update/<int:pk>', AdvUpdateView.as_view(), name = 'adv-update'),
    path('adv/delete/<int:pk>', AdvDeleteView.as_view(), name = 'adv-delete'),

    path('config/index', ConfigIndexView.as_view(), name = 'config-index'),
    path('config/create', ConfigCreateView.as_view(), name = 'config-create'),
    path('config/update/<int:pk>', ConfigUpdateView.as_view(), name = 'config-update'),
    path('config/delete/<int:pk>', ConfigDeleteView.as_view(), name = 'config-delete'),

    path('feedback/index', FeedbackIndexView.as_view(), name = 'feedback-index'),
    path('feedback/view/<int:pk>', FeedbackDetailView.as_view(), name = 'feedback-view'),
    path('feedback/delete/<int:pk>', FeedbackDeleteView.as_view(), name = 'feedback-delete'),

    path('friend-link/index', FriendLinkIndexView.as_view(), name = 'friend-link-index'),
    path('friend-link/create', FriendLinkCreateView.as_view(), name = 'friend-link-create'),
    path('friend-link/update/<int:pk>', FriendLinkUpdateView.as_view(), name = 'friend-link-update'),
    path('friend-link/delete/<int:pk>', FriendLinkDeleteView.as_view(), name = 'friend-link-delete'),

    path('category/index', CategoryIndexView.as_view(), name = 'category-index'),
    path('category/create', CategoryCreateView.as_view(), name = 'category-create'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name = 'category-update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name = 'category-delete'),

    path('posts/index', PostsIndexView.as_view(), name = 'posts-index'),
    path('posts/create', PostsCreateView.as_view(), name = 'posts-create'),
    path('posts/update/<int:pk>', PostsUpdateView.as_view(), name = 'posts-update'),
    path('posts/delete/<int:pk>', PostsDeleteView.as_view(), name = 'posts-delete'),

    path('article/index', ArticleIndexView.as_view(), name = 'article-index'),
    path('article/create', ArticleCreateView.as_view(), name = 'article-create'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name = 'article-update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name = 'article-delete'),

    path('product/index', ProductIndexView.as_view(), name = 'product-index'),
    path('product/create', ProductCreateView.as_view(), name = 'product-create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name = 'product-update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name = 'product-delete'),

    #path('adv/index', AdvView.index),
    #path('adv/create', AdvView.create),
    #path('adv/update/<int:id>', AdvView.update),
    #path('adv/delete/<int:id>', AdvView.delete),

]