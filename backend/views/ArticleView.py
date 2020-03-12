from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Article import Article
from backend.forms.ArticleForm import ArticleForm

class ArticleIndexView(BackendLoginRequiredMinix, ListView):
    model = Article # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = 20 # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'article/index.html'

    def get_queryset(self):
        cid = self.request.GET.get('cid', None)
        queryset  = super().get_queryset()
        if cid is not None:
            queryset = Article.objects.filter(category_id = cid).order_by('-id')
        return queryset

    
    def get_context_data(self, **kwargs):
        cid = self.request.GET.get('cid', None)
        context = super().get_context_data(**kwargs)
        if cid is not None:
            context['cid'] = cid
        return context

class ArticleCreateView(BackendLoginRequiredMinix, CreateView):
    model = Article # 指定模型
    template_name = 'article/create.html'
    form_class = ArticleForm


class ArticleUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = Article # 指定模型
    template_name = 'article/update.html'
    form_class = ArticleForm

    #def get(self, request, *args, **kwargs):
    #    adv_positin = Article.objects.get(id = self.kwargs['pk'])
    #    #form = self.form_class(instance=adv_positin)
    #    form = ArticleForm(instance=adv_positin)
    #    return render(request, self.template_name, {'form': form})
    

class ArticleDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = Article
    #success_url = '/backend/article/index'

    def post(self, request, *args, **kwargs):
        adv_position = Article.objects.get(id = self.kwargs['pk'])
        adv_position.status = 0 if adv_position.status == 8 else 8
        adv_position.save()
        return redirect('/backend/article/index')
   

        
