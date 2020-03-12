from django.forms.widgets import RadioSelect, Input
import json

class TyRadioSelect(RadioSelect):
    template_name = '../templates/widgets/radio.html'
    option_template_name = '../templates/widgets/radio_option.html'


class TyFileInput(Input):
    media_list = None
    def __init__(self, attrs=None, media_list=None):
        super().__init__(attrs)
        self.media_list = media_list

    template_name = '../templates/widgets/file.html'
    
    def format_value(self, value):
        if isinstance(value, list):
            photo_ids = ''
            if len(value) > 0:
                photo_ids_list = []
                for val in value:
                    photo_ids_list.append(val.id)
                photo_ids = json.dumps(photo_ids_list)
            return photo_ids
        else:
            value = super().format_value(value)
            return str(value)

        
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
       
        if 'media_list' not in context:
            context['media_list'] = self.media_list
        return context


class TyEditorInput(Input):
    template_name = '../templates/widgets/editor.html'