from api.models import Article
from django.contrib.auth.models import User


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data

