from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from backend.widgets.TyWidgets import TyEditorInput
from common.models import Category

class PostsForm(BootstrapModelForm):

    class Meta:
        model = Category
        fields = ['name', 'content']
        widgets = {
            "name": widget.Input(attrs={'class':'form-control', 'readonly': 'readonly'}),
            "content": TyEditorInput(attrs={'class':'form-control'}),
        }  