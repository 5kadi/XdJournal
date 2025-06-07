from django.db import models
from django.contrib import auth
from django.dispatch import receiver
from api.article.models import Article
import os


def get_filepath(instance, filename):
    path = os.path.join(f"user_{instance.user.id}", f"article_{instance.user.id}", filename)
    return path

class Media(models.Model):
    user = models.ForeignKey(to=auth.get_user_model(), on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s") #creator (User)
    content = models.FileField(upload_to=get_filepath) #media itself
    class Meta:
        abstract = True


class ArticleMedia(Media):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s') #parent article

#class AvatarMedia(Media): ...


@receiver(models.signals.post_delete)
def media_delete(sender: Media, instance: Media, **kwargs):
    if isinstance(instance, Media): 
        os.remove(instance.content.path)
