from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView
from django.contrib.auth import authenticate, login, logout

class LoginView(TemplateView):
    template_name = 'site/login.html'


class LoginInView(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('login')
        password = request.POST.get('secret')
        code = request.POST.get('code')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/backend/config/index')
        else:
            return redirect('/backend/login')

class LoginOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/backend/login')
