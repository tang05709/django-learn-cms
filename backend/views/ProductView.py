from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Product import Product
from common.models.ProductPhoto import ProductPhoto
from backend.forms.ProductForm import ProductForm

class ProductIndexView(BackendLoginRequiredMinix, ListView):
    model = Product # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = 20 # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'product/index.html'

    def get_queryset(self):
        cid = self.request.GET.get('cid', None)
        queryset  = super().get_queryset()
        if cid is not None:
            queryset = Product.objects.filter(category_id = cid).order_by('-id')
        return queryset

    
    def get_context_data(self, **kwargs):
        cid = self.request.GET.get('cid', None)
        context = super().get_context_data(**kwargs)
        if cid is not None:
            context['cid'] = cid
        return context

class ProductCreateView(BackendLoginRequiredMinix, CreateView):
    model = Product # 指定模型
    template_name = 'product/create.html'
    form_class = ProductForm

class ProductUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = Product # 指定模型
    template_name = 'product/update.html'
    form_class = ProductForm

    #def get(self, request, *args, **kwargs):
    #    adv_positin = Product.objects.get(id = self.kwargs['pk'])
    #    #form = self.form_class(instance=adv_positin)
    #    form = ProductForm(instance=adv_positin)
    #    return render(request, self.template_name, {'form': form})
    

class ProductDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = Product
    #success_url = '/backend/product/index'

    def post(self, request, *args, **kwargs):
        adv_position = Product.objects.get(id = self.kwargs['pk'])
        adv_position.status = 0 if adv_position.status == 8 else 8
        adv_position.save()
        return redirect('/backend/product/index')
   

        
