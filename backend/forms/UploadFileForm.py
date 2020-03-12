from .BaseForm import BootstrapModelForm
from common.models import Attachment

class UploadFileForm(BootstrapModelForm):
    class Meta:
        model = Attachment
        fields = ['name']