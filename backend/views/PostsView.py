from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Category import Category
from backend.forms.PostsForm import PostsForm


class PostsIndexView(BackendLoginRequiredMinix, UpdateView):
    model = Category # 指定模型
    template_name = 'posts/update.html'
    form_class = PostsForm

    def get(self, request, *args, **kwargs):
        cid = self.request.GET.get('cid', None)
        posts = Category.objects.get(id = cid)
        #form = self.form_class(instance=adv_positin)
        form = PostsForm(instance=posts)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        cid = self.request.GET.get('cid', None)
        content = self.request.POST.get('content', None)
        if content is not None:
            posts = Category.objects.get(id = cid)
            posts.content = content
            posts.save()
        return redirect('/backend/posts/index?cid=' + cid)


    
        
