from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from backend.widgets.TyWidgets import TyRadioSelect
from common.models import Posts
from backend.forms.CategoryForm import treeview2

class PostsForm(BootstrapModelForm):
    def __init__(self, *args, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)

        self.fields['category'].choices = treeview2()

    class Meta:
        model = Posts
        fields = ['title', 'category', 'seo_title', 'seo_keywords', 'seo_description', 'content', 'status']
        widgets = {
            "seo_description": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
            "status":TyRadioSelect(attrs={'class':'customer-form-radio'}),
            "content": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
        }  