from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from backend.widgets.TyWidgets import TyRadioSelect
from common.models import AdvPosition

class AdvPositionForm(BootstrapModelForm):
    class Meta:
        model = AdvPosition
        fields = ['name', 'status']
        widgets = {
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
        }  