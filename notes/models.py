from django.db import models
from allauth.account.models import get_user_model
from django.conf import settings

# Create your models here.
class Tags(models.Model):
    
    tag_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "tags"
        
    def __str__(self):
        return self.tag_name
    


class Notes(models.Model):
    class Meta:
        verbose_name_plural = "Notes" 
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Notes')
    title = models.CharField(max_length=255)
    content = models.TextField()
    note_image = models.ImageField(upload_to='note_image', default='default_note_image.png', blank=True, null=True)
    public = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tags, related_name='Notes')
    views_count = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Note")
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title



class Comments(models.Model):
    class Meta:
        verbose_name_plural = "Comments"
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments', blank=True)
    disliked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='disliked_comments',blank=True)
    
    @property
    def like_count(self):
        return self.liked_by.count()
    
    @property
    def dislike_count(self):
        return self.disliked_by.count()
    
    def __str__(self):
        return self.comment


    
    
