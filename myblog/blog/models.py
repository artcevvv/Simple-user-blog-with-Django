from django.db import models
from tinymce import models as tinymce_models


# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=255)
    slug= models.SlugField()
    intro= models.TextField()
    body= tinymce_models.HTMLField()
    date= models.DateField(auto_now_add=True)
    image= models.ImageField(null= True, blank=True)

    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url= ''
        return url
        

    class Meta:
        ordering= ['-date']

class Comment(models.Model):
    post= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    body= models.CharField(max_length=10000)
    date= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-date']


