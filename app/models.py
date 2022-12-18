from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField() #post_content
    created_at = models.DateTimeField(auto_now_add=True)
    #edited bin
    updated_at = models.DateTimeField(auto_now=True)
    #summary = models.CharField(max_length=250)
    #post_user INT

    def __str__(self):
        return self.title
