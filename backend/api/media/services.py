from .models import Media, ArticleMedia
from api.article.models import Article

def push_content(article_obj: Article, frag_id: str, frag_content: dict): #its ensured that object exists
    article_obj.content[frag_id] = frag_content
    article_obj.save()

