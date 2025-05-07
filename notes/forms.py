from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['author', 'title', 'content', 'note_image', 'public']
        widgets = {
            "title": forms.TextInput(attrs={
                "class":"form-control",
                "id":"note-title",
                "type": "text",
                "placeholder": "Enter a descriptive title"
            }),
            
            "content": forms.Textarea(attrs={
                "class":"form-control",
                "id":"note-content",
                "placeholder": "Write your note here..."
            }),
            
            "note_image": forms.FileInput(attrs={
                "id":"note-image",
                "type": "file",
                "accept": "image/*",
            }),
            
            "public": forms.CheckboxInput(attrs={
                "type":"checkbox",
                "name":"private",
                "id": "note-public"
            })
        }
        
     
        
class EditNoteForm(forms.ModelForm):  
    class Meta:
        model = Notes
        fields = ['title','content', 'note_image', 'public']
        widgets = {
            "title": forms.TextInput(attrs={
                "class":"form-control",
                "id":"note-title",
                "type": "text",
                "placeholder": "Enter a descriptive title"
            }),
            
            "content": forms.Textarea(attrs={
                "class":"form-control",
                "id":"note-content",
                "placeholder": "Write your note here..."
            }),
            
            "note_image": forms.FileInput(attrs={
                "id":"note-image",
                "type": "file",
                "accept": "image/*",
                "required": False,
            }),
            
            "public": forms.CheckboxInput(attrs={
                "type":"checkbox",
                "name":"private",
                "id": "note-public"
            })
        }
