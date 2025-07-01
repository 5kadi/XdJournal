from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from api.article.models import Article


class Comment(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s') #TODO: make it work witth models.DO_NOTHING
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s')
    create_date = models.DateTimeField(db_index=True, default=timezone.now) 
    update_date = models.DateTimeField(auto_now=True) 
    content = models.TextField(blank=False)

    #NOTE:
    #content's newline characters are saved as \n, so you should replace then in frontend (style="white-space: pre-line;")

