from django.core.exceptions import ObjectDoesNotExist
from .models import Media
from api.article.models import Article
from backend.settings import MEDIA_URL
from urllib import parse


def get_by_content(article_obj: Article, content: str) -> Media | None:
    content = parse.unquote_plus(content.split(MEDIA_URL)[-1])
    try:
        #related_name='%(app_label)s_%(class)s' in api.media.models
        media_obj = article_obj.api_articlemedia.get(content=content) 
    except ObjectDoesNotExist:
        return None
    else:
        return media_obj