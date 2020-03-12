from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from backend.helps.BackendLoginRequiredMinix import BackendLoginRequiredMinix
from common.models.FriendLink import FriendLink
from backend.forms.FriendLinkForm import FriendLinkForm

class FriendLinkIndexView(BackendLoginRequiredMinix, ListView):
    model = FriendLink # 指定模型
    context_object_name = 'grid' # 默认object_list
    paginate_by = False # 每页显示数量 默认Paginator实例 page_obj
    ordering = ['-id'] # 默认排序
    template_name = 'friend-link/index.html'

class FriendLinkCreateView(BackendLoginRequiredMinix, CreateView):
    model = FriendLink # 指定模型
    template_name = 'friend-link/create.html'
    form_class = FriendLinkForm


class FriendLinkUpdateView(BackendLoginRequiredMinix, UpdateView):
    model = FriendLink # 指定模型
    template_name = 'friend-link/update.html'
    form_class = FriendLinkForm
    

class FriendLinkDeleteView(BackendLoginRequiredMinix, DeleteView):
    #model = FriendLink
    #success_url = '/backend/friend-link/index'

    def post(self, request, *args, **kwargs):
        friend_link = FriendLink.objects.get(id = self.kwargs['pk'])
        friend_link.status = 0 if friend_link.status == 8 else 8
        friend_link.save()
        return redirect('/backend/friend-link/index')
   
