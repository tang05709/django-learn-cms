from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from django.forms import fields
from backend.widgets.TyWidgets import TyRadioSelect, TyFileInput, TyEditorInput
from common.models import Product, Attachment
from backend.forms.CategoryForm import treeview2
import json

class ProductForm(BootstrapModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        self.fields['category'].choices = treeview2()

        photos = []
        if not self.instance._state.adding and self.instance.photos.all():
            for photo in self.instance.photos.all():
                photos.append(photo.url)
                
                
        self.fields['photos'] = fields.CharField(label = '画册', widget = TyFileInput(attrs={'class': "customer-form-file media-picker-button", 'data-upload-path': 'product', 'data-multiple': 'multiple', 'id': 'photos_uploader'}, media_list = photos))

    def clean_photos(self):
        photos = self.cleaned_data['photos']
        clean_photos = []
        if photos != '':
            photos_arr = json.loads(photos)
            for photo in photos_arr:
                attachment = Attachment.objects.get(id=photo)
                clean_photos.append(attachment)

        return clean_photos

    class Meta:
        model = Product
        fields = ['title', 'category', 'status', 'price', 'photos', 'seo_title', 'seo_keywords', 'seo_description', 'content']
        widgets = {
            "seo_description": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
            "content": TyEditorInput(attrs={'class':'form-control'}),
        }  