from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Category import Category
from backend.forms.CategoryForm import CategoryForm
from backend.helps.TreeView import TreeView

class CategoryIndexView(BackendLoginRequiredMinix, ListView):
    model = Category # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = False # 每页显示数量 默认Paginator实例 page_obj
    #ordering = ['-id'] # 默认排序
    template_name = 'category/index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.order_by('sort').all()
        treeView = TreeView()
        queryset = treeView.ListTree(categories.values())
        return render(request, self.template_name, {'grid': queryset})

class CategoryCreateView(BackendLoginRequiredMinix, CreateView):
    model = Category # 指定模型
    template_name = 'category/create.html'
    form_class = CategoryForm


class CategoryUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = Category # 指定模型
    template_name = 'category/update.html'
    form_class = CategoryForm

    #def get(self, request, *args, **kwargs):
    #    adv_positin = Category.objects.get(id = self.kwargs['pk'])
    #    #form = self.form_class(instance=adv_positin)
    #    form = CategoryForm(instance=adv_positin)
    #    return render(request, self.template_name, {'form': form})
    

class CategoryDeleteView(BackendLoginRequiredMinix, DeleteView):
    model = Category
    success_url = '/backend/category/index'   
