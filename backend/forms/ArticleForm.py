from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from django.forms import fields
from backend.widgets.TyWidgets import TyRadioSelect, TyFileInput, TyEditorInput
from common.models import Article
from backend.forms.CategoryForm import treeview2

class ArticleForm(BootstrapModelForm):
    #self.instance.image
    #image = fields.CharField(widget = TyFileInput(attrs={'class': "customer-form-file media-picker-button", 'data-upload-path': 'article', 'id': 'image_uploader'}, media_list = {'dd': models.instance.image}))

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['category'].choices = treeview2()

        images = []
        if self.instance.image:
            images = [self.instance.image.url]
        self.fields['image'] = fields.CharField(label = '图片', widget = TyFileInput(attrs={'class': "customer-form-file media-picker-button", 'data-upload-path': 'article', 'id': 'image_uploader'}, media_list = images))

    class Meta:
        model = Article
        fields = ['title', 'category', 'status', 'url', 'image', 'seo_title', 'seo_keywords', 'seo_description', 'content']
        widgets = {
            "seo_description": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
            "content": TyEditorInput(attrs={'class':'form-control'}),
        }  