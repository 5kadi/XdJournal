from api.models import Article
import json
from rest_framework.response import Response
from django.contrib.auth.models import User


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data


def push_content(id: int, content: str):
    article_obj = Article.objects.get(pk=id)
    article_content_D: list = json.loads(article_obj.content)
    article_content_D.append({"type": "media", "content": content})
    print(article_content_D)
    article_obj.content = json.dumps(article_content_D)
    article_obj.save()