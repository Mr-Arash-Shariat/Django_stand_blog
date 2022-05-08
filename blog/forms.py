from django import forms
from . import models
from django.core.validators import ValidationError



class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='Your Name')
    text = forms.CharField(max_length=10, label='Your Message')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('Name and Text are same.', code='name_text_same')



class MessageForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput())
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     "class": "form-control"
    # }))

    class Meta:
        model = models.Message
        fields = '__all__'

        # Special widgets
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter your title..."
            }),
            "text": forms.Textarea(attrs={
                "placeholder": "Enter the text of your message in this box..."
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Please enter the valid email..."
            })
        }

    # Widget for all
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
       