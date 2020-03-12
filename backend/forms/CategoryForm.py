from .BaseForm import BootstrapModelForm
from django.forms import widgets as widget
from django.forms.fields import ChoiceField
from backend.widgets.TyWidgets import TyRadioSelect
from common.models import Category
from backend.helps.TreeView import TreeView


def treeview():
    categories = Category.objects.all()
    treeView = TreeView()
    tree = treeView.ListOptions(categories.values())
    tree.insert(0, ['', '顶级栏目'])
    return tree

def treeview2():
    categories = Category.objects.all()
    treeView = TreeView()
    tree = treeView.ListOptions(categories.values())
    tree.insert(0, ['', '请选择'])
    return tree


class CategoryForm(BootstrapModelForm):
    #parent = ChoiceField(choices = treeview(), label = '父级')
    #parent = ChoiceField(choices = treeview(), label = '父级')
    #print(parent)
    
    def __init__(self,*args,**kwargs):
        super(CategoryForm,self).__init__(*args,**kwargs)
        self.fields['parent'].choices = treeview()
    

    '''
    def clean_parent(self):
        parent = int(self.cleaned_data['parent'])
        if parent > 0:
            return Category.objects.get(id = parent)

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return None
    '''
    
    

    class Meta:
        model = Category
        fields = ['name', 'module', 'parent', 'seo_title', 'seo_keywords', 'seo_description', 'sort', 'status']
        widgets = {
            "status": TyRadioSelect(attrs={'class':'customer-form-radio'}),
            "seo_description": widget.Textarea(attrs={'class':'form-control', 'rows': 5}),
        }  
        