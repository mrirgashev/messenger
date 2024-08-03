from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['messege']
        widgets = {
            'messege': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Type your message...'}),
        }