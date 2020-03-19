
from .BaseForm import BootstrapModelForm
from backend.widgets.TyWidgets import TyRadioSelect, TyFileInput
from django.forms import fields
from common.models import FriendLink

class FriendLinkForm(BootstrapModelForm):
    def __init__(self, *args, **kwargs):
        super(FriendLinkForm, self).__init__(*args, **kwargs)

        images = []
        if self.instance.logo:
            images = [self.instance.logo.url]
        self.fields['logo'] = fields.CharField(label = 'logo', widget = TyFileInput(attrs={'class': "customer-form-file media-picker-button", 'data-upload-path': 'logo', 'id': 'logo_uploader'}, media_list = images))
    
    def clean_image(self):
        logo = self.cleaned_data['logo']
        if logo is None:
            return 0
        return logo
    
    class Meta:
        model = FriendLink
        fields = ['name', 'url', 'logo', 'sort', 'status']
        widgets = {
            "logo":TyFileInput(attrs={'class':'customer-form-file media-picker-button', 'data-upload-path': 'common', 'id': 'logo_uploader'}, media_list = {'dd': 'ss'}),
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
        } 
