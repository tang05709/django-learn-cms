
from django.contrib.auth.mixins import LoginRequiredMixin

class BackendLoginRequiredMinix(LoginRequiredMixin):
    login_url = '/backend/login'
    redirect_field_name = 'redirect_to'