from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Adv import Adv
from backend.forms.AdvForm import AdvForm

class AdvIndexView(BackendLoginRequiredMinix, ListView):
    model = Adv # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = False # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'adv/index.html'

class AdvCreateView(BackendLoginRequiredMinix, CreateView):
    model = Adv # 指定模型
    template_name = 'adv/create.html'
    form_class = AdvForm


class AdvUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = Adv # 指定模型
    template_name = 'adv/update.html'
    form_class = AdvForm
    

class AdvDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = Adv
    #success_url = '/backend/adv/index'
    
    def post(self, request, *args, **kwargs):
        adv = Adv.objects.get(id = self.kwargs['pk'])
        adv.status = 0 if adv.status == 8 else 8
        adv.save()
        return redirect('/backend/adv/index')
   
