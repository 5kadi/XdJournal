from django.db import models
from django.contrib import auth
from django.dispatch import receiver
from api.article.models import Article
import os


def get_filepath(instance, filename):
    path = os.path.join(f"author_{instance.user.id}", f"article_{instance.user.id}", filename)
    return path

class Media(models.Model):
    user = models.ForeignKey(to=auth.get_user_model(), on_delete=models.CASCADE, related_name='media') #creator (User)
    content = models.FileField(upload_to=get_filepath) #media itself
    class Meta:
        abstract = True

class ArticleMedia(Media):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='media') #parent article
    frag_id = models.CharField(max_length=30, default=None)

#class AvatarMedia(Media): ...


@receiver(models.signals.post_delete, sender=Media)
def media_delete(sender: Media, instance: Media, **kwargs):
    if instance.content:
        print(instance.content.path)
        #if os.path.isfile(instance.content.path):
        os.remove(instance.content.path)
    return
