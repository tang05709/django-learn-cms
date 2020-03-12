
from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from backend.widgets.TyWidgets import TyFileInput, TyRadioSelect
from common.models import Adv, AdvPosition

class AdvForm(BootstrapModelForm):
    class Meta:
        model = Adv
        fields = ['name', 'adv_position', 'url', 'image', 'sort', 'status', 'describe']
        widgets = {
            "image": TyFileInput(attrs={'class':'customer-form-file media-picker-button', 'data-upload-path': 'adv', 'id': 'image_uploader'}),
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
            "describe": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
        }