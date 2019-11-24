from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(help_text='enter your post here')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:20] + '...'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
