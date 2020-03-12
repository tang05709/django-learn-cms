
from .BaseForm import BootstrapModelForm
from backend.widgets.TyWidgets import TyRadioSelect, TyFileInput
from common.models import FriendLink

class FriendLinkForm(BootstrapModelForm):
    required_css_class = 'required'
    
    class Meta:
        model = FriendLink
        fields = ['name', 'url', 'logo', 'sort', 'status']
        widgets = {
            "logo":TyFileInput(attrs={'class':'customer-form-file media-picker-button', 'data-upload-path': 'common', 'id': 'logo_uploader'}, media_list = {'dd': 'ss'}),
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
        } 
