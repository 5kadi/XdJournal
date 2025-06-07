from django.core.exceptions import ObjectDoesNotExist
from .models import Media
from api.article.models import Article
from backend.settings import MEDIA_URL
from urllib import parse


def get_by_content(article_obj: Article, content: str) -> Media | None:
    content = parse.unquote_plus(content.split(MEDIA_URL)[-1])
    try:
        media_objs = article_obj.api_articlemedia.all()
        media_obj = media_objs.get(content=content)
    except ObjectDoesNotExist:
        return None
    else:
        return media_obj