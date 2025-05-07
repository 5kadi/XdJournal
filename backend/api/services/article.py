from api.models import Article
import json
import jsonschema
from rest_framework.response import Response
from django.contrib.auth.models import User


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data


def push_content(article_id: int, frag_id: str, frag_content: dict):
    article_obj = Article.objects.get(pk=article_id) #its ensured that object exists
    article_obj.content[frag_id] = frag_content
    article_obj.save()

def content_frag_is_valid(content_frag):
    schema = Article.CONTENT_SCHEMA
    try:
        jsonschema.validate(content_frag, schema)
    except jsonschema.ValidationError as e:
        print(e)
        return False
    else:
        return True
    
