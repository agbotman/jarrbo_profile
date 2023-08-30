from django.utils.translation import gettext as _
from django import forms
from jarrbo_theme.forms import JarrboFormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):
    name = forms.CharField(label=_("Name"), required=True)
    email = forms.EmailField(label=_("Your email address"), required=True)
    subject = forms.CharField(label=_("Subject"), required=True)
    message = forms.CharField(
        label=_("Message"),
        required=True,
        widget=forms.Textarea
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = JarrboFormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _('Submit')))
        
