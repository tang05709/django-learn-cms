
from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from backend.widgets.TyWidgets import TyFileInput, TyRadioSelect
from django.forms import fields
from common.models import Adv

class AdvForm(BootstrapModelForm):
    def __init__(self, *args, **kwargs):
        super(AdvForm, self).__init__(*args, **kwargs)

        images = []
        if self.instance.image:
            images = [self.instance.image.url]
        self.fields['image'] = fields.CharField(label = '图片', widget = TyFileInput(attrs={'class': "customer-form-file media-picker-button", 'data-upload-path': 'adv', 'id': 'image_uploader'}, media_list = images))
    
    def clean_image(self):
        image = self.cleaned_data['image']
        if image is None:
            return 0
        return image

    class Meta:
        model = Adv
        fields = ['name', 'adv_position', 'url', 'image', 'sort', 'status', 'describe']
        widgets = {
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
            "describe": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
        }