from common.models.Category import Category
from backend.helps.TreeView import TreeView

def navigation(request):
    categories = Category.objects.order_by('sort').filter(status = 0)
    treeView = TreeView()
    navigations = treeView.ListLayerTree(categories.values())
    return {"navigations": navigations}