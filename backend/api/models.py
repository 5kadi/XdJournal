from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser
from .utils import model_utils
import os



#class Author(auth.models.AbstractBaseUser):



#Article
ARTICLE_CONTENT_SCHEMA = {
        "type": "object",
        "patternProperties": {
                r"^[A-Za-z0-9]+": {
                "type": "object", 
                "properties": {
                    "type": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["type", "content"],
                "additionalProperties": False
            }
        }
    } 

class Article(models.Model):
    author = models.ForeignKey(to=auth.get_user_model(), on_delete=models.CASCADE, related_name='articles') #creator (User)
    create_date = models.DateTimeField(db_index=True, default=timezone.now) #creation date
    update_date = models.DateTimeField(auto_now=True) #last update date
    header = models.CharField(max_length=100, default="Unnamed article")
    content = models.JSONField(default=model_utils.default_content) #article text (XdMD)
    is_published = models.BooleanField(default=False) 

    #@property
    #def related_media(self):
        #return self.media.all()

#Media
class Media(models.Model):
    author = models.ForeignKey(to=auth.get_user_model(), on_delete=models.CASCADE, related_name='media') #creator (User)
    content = models.FileField(upload_to=model_utils.get_filepath) #media itself
    class Meta:
        abstract = True

class ArticleMedia(Media):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='media') #parent article
    frag_id = models.CharField(max_length=30, default=None)

class AvatarMedia(Media): ...


@receiver(models.signals.post_delete, sender=Media)
def media_delete(sender: Media, instance: Media, **kwargs):
    if instance.content:
        print(instance.content.path)
        #if os.path.isfile(instance.content.path):
        os.remove(instance.content.path)
    return



