from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.Feedback import Feedback

class FeedbackIndexView(BackendLoginRequiredMinix, ListView):
    model = Feedback # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = 20 # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'feedback/index.html'

    def get_queryset(self):
        cid = self.request.GET.get('cid', None)
        queryset  = super().get_queryset()
        if cid is not None:
            queryset = Feedback.objects.filter(category_id = cid).order_by('-id')
        return queryset

    
    def get_context_data(self, **kwargs):
        cid = self.request.GET.get('cid', None)
        context = super().get_context_data(**kwargs)
        if cid is not None:
            context['cid'] = cid
        return context

class FeedbackDetailView(BackendLoginRequiredMinix, DetailView):
    model = Feedback
    context_object_name = 'detail'
    template_name = 'feedback/view.html'

class FeedbackDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = Feedback
    #success_url = '/backend/feedback/index'

    def post(self, request, *args, **kwargs):
        feedback = Feedback.objects.get(id = self.kwargs['pk'])
        feedback.status = 0 if feedback.status == 8 else 8
        feedback.save()
        return redirect('/backend/feedback/index')