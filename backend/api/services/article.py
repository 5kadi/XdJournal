from api.models import ARTICLE_CONTENT_SCHEMA, Article
import jsonschema
from django.contrib.auth.models import AbstractBaseUser


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data

def check_ownership(article_obj: Article, user: AbstractBaseUser):
    if article_obj.author == user:
        return True
    else:
        return False

def push_content(article_obj: Article, frag_id: str, frag_content: dict): #its ensured that object exists
    article_obj.content[frag_id] = frag_content
    article_obj.save()

def content_frag_is_valid(content_frag: dict):
    schema = ARTICLE_CONTENT_SCHEMA
    try:
        jsonschema.validate(content_frag, schema)
    except jsonschema.ValidationError as e:
        #print(e)
        return False
    else:
        return True


    
