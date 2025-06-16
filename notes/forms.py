from django import forms
from .models import Notes
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

class NotesForm(forms.ModelForm):
    """model form for creating new notes."""
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
        
    def clean_note_image(self):
        image = self.cleaned_data.get('note_image')
        max_size_mb = 5

        if isinstance(image, UploadedFile):
            if image:
                if image.size > max_size_mb * 1024 * 1024:
                    raise ValidationError(f"note_image size cannot exceed {max_size_mb}MB.")
        return image 
        
     
        
class EditNoteForm(forms.ModelForm): 
    """model form for editing existing notes.""" 
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
    
    def clean_note_image(self):
        image = self.cleaned_data.get('note_image')
        max_size_mb = 5

        if isinstance(image, UploadedFile):
            if image:
                if image.size > max_size_mb * 1024 * 1024:
                    raise ValidationError(f"note_image size cannot exceed {max_size_mb}MB.")
        return image 
        
