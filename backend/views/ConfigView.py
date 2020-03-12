from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Config import Config
from backend.forms.ConfigForm import ConfigForm

class ConfigIndexView(BackendLoginRequiredMinix, ListView):
    model = Config # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = False # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'config/index.html'

class ConfigCreateView(BackendLoginRequiredMinix, CreateView):
    model = Config # 指定模型
    template_name = 'config/create.html'
    form_class = ConfigForm


class ConfigUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = Config # 指定模型
    template_name = 'config/update.html'
    form_class = ConfigForm
    

class ConfigDeleteView(BackendLoginRequiredMinix, DeleteView):
    model = Config
    success_url = '/backend/config/index'
   
