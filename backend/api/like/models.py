from django.db import models
from django.contrib.auth import get_user_model
from api.article.models import Article
from api.comment.models import Comment

#idgaf about inheritance/DRY here, cause only 2 models eksdi
class ArticleLike(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s') #TODO: make it work witth models.DO_NOTHING
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s')

    class Meta:
        unique_together = ["user", "article"]

class CommentLike(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s') #TODO: make it work witth models.DO_NOTHING
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s')

    class Meta:
        unique_together = ["user", "comment"]