
from .BaseForm import BootstrapModelForm
from common.models import Config

class ConfigForm(BootstrapModelForm):
    class Meta:
        model = Config
        fields = ['ckey', 'cvalue']