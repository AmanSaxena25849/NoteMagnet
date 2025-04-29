from django.db import models
from allauth.account.models import get_user_model

# Create your models here.

user = get_user_model()

class Tags(models.Model):
    
    tag_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "tags"
        
    def __str__(self):
        return self.tag_name
    
    

class Notes(models.Model):
    
    class Meta:
        verbose_name_plural = "Notes" 
    
    author = models.ForeignKey(user, on_delete=models.CASCADE, related_name='Notes')
    title = models.CharField(max_length=255)
    content = models.TextField()
    note_image = models.ImageField(upload_to='note_image',blank=True, null=True)
    public = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tags, related_name='Notes')
    views_count = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title



    
    
