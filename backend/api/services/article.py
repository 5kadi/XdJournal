from api.models import Article


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data