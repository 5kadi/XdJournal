from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from .services.path import get_filepath

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='articles') #creator (User)
    create_date = models.DateTimeField(db_index=True, default=timezone.now) #creation date
    update_date = models.DateTimeField(auto_now=True) #last update date
    header = models.CharField(max_length=100, default="Unnamed article")
    text_content = models.TextField() #article text (XdMD)
    is_published = models.BooleanField(default=False)

    #@property
    #def related_media(self):
        #return self.media.all()

class Media(models.Model):
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='media') #creator (User)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='media') #parent article
    token = models.CharField(max_length=10) #position of image in an article
    content = models.FileField(upload_to=get_filepath) #media itself




