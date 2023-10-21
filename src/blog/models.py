from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=36)
    slug=models.SlugField()

class BlogPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    title=models.CharField(max_length=36)
    slug=models.SlugField()
    content=models.TextField()
    published=models.BooleanField(default=False)
    date=models.DateTimeField(blank=True,null=True)
    description=models.TextField()

    def publish_string(self):
        if self.published:
            return "l'article est publié"
        return "l'article est introuvable"


