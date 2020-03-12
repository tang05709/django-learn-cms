from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Posts import Posts
from backend.forms.PostsForm import PostsForm

class PostsIndexView(BackendLoginRequiredMinix, ListView):
    model = Posts # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = 20 # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'posts/index.html'

    def get_queryset(self):
        cid = self.request.GET.get('cid', None)
        queryset  = super().get_queryset()
        if cid is not None:
            queryset = Posts.objects.filter(category_id = cid).order_by('-id')
        return queryset

    
    def get_context_data(self, **kwargs):
        cid = self.request.GET.get('cid', None)
        context = super().get_context_data(**kwargs)
        if cid is not None:
            context['cid'] = cid
        return context

class PostsCreateView(BackendLoginRequiredMinix, CreateView):
    model = Posts # 指定模型
    template_name = 'posts/create.html'
    form_class = PostsForm


class PostsUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = Posts # 指定模型
    template_name = 'posts/update.html'
    form_class = PostsForm

    #def get(self, request, *args, **kwargs):
    #    adv_positin = Posts.objects.get(id = self.kwargs['pk'])
    #    #form = self.form_class(instance=adv_positin)
    #    form = PostsForm(instance=adv_positin)
    #    return render(request, self.template_name, {'form': form})
    

class PostsDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = Posts
    #success_url = '/backend/posts/index'

    def post(self, request, *args, **kwargs):
        posts = Posts.objects.get(id = self.kwargs['pk'])
        posts.status = 0 if posts.status == 8 else 8
        posts.save()
        return redirect('/backend/posts/index')
   

        
