from django import forms 

class BootstrapModelForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if('class' in self.fields[field].widget.attrs):
                if(self.fields[field].widget.attrs['class'] == 'customer-form-radio'):
                    self.fields[field].widget.attrs.update({
                        'class': 'customer-form-radio'
                    })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

                
    
    def as_div(self):
        "bootstrap."
        """
        bootstrap
        <div class="form-group row">
        <label class="col-sm-2 col-form-label">label</label>
        <div class="col-sm-10">
           input
           <div class="help-block">help</div>
        </div>
        </div>
        """
        return self._html_output(
            normal_row='<div class="form-group row %(html_class_attr)s"><div class="col-sm-2 col-form-label text-right">%(label)s</div><div class="col-sm-10">%(field)s%(help_text)s%(errors)s</div></div>',
            #normal_row='<li%(html_class_attr)s>%(errors)s%(label)s %(field)s%(help_text)s</li>',
            error_row='<div class="error">%s</div>',
            row_ender='</div>',
            help_text_html=' <div class="help-block">%s</div>',
            errors_on_separate_row=False,
        )