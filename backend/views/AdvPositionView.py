from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.AdvPosition import AdvPosition
from backend.forms.AdvPositionForm import AdvPositionForm

class AdvPositionIndexView(BackendLoginRequiredMinix, ListView):
    model = AdvPosition # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = False # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'adv-position/index.html'

class AdvPositionCreateView(BackendLoginRequiredMinix, CreateView):
    model = AdvPosition # 指定模型
    template_name = 'adv-position/create.html'
    form_class = AdvPositionForm


class AdvPositionUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = AdvPosition # 指定模型
    template_name = 'adv-position/update.html'
    form_class = AdvPositionForm

    #def get(self, request, *args, **kwargs):
    #    adv_positin = AdvPosition.objects.get(id = self.kwargs['pk'])
    #    #form = self.form_class(instance=adv_positin)
    #    form = AdvPositionForm(instance=adv_positin)
    #    return render(request, self.template_name, {'form': form})
    

class AdvPositionDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = AdvPosition
    #success_url = '/backend/adv-position/index'

    def post(self, request, *args, **kwargs):
        adv_position = AdvPosition.objects.get(id = self.kwargs['pk'])
        adv_position.status = 0 if adv_position.status == 8 else 8
        adv_position.save()
        return redirect('/backend/adv-position/index')
   

        
