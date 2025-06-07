from .models import ARTICLE_CONTENT_SCHEMA, Article
import jsonschema


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data

def insert_block(article_obj: Article, block_id: int, block: dict):
    article_content: list = article_obj.content
    if block_id < len(article_content):
        article_content.insert(block_id, block)
    else:
        article_content.append(block)
    article_obj.save()

def pop_block(article_obj: Article, block_id: int) -> dict | None:
    article_content: list = article_obj.content
    if len(article_content) > 1:
        block = article_content.pop(block_id)
        article_obj.save()
        return block
    else:
        return None

def modify_content(article_obj: Article, block_id: int, block: dict): #its ensured that object exists
    article_content: list = article_obj.content
    if block_id < len(article_content):
        article_content[block_id] = block
    else:
        article_content.append(block)
    article_obj.save()


def block_is_valid(block: dict):
    schema = ARTICLE_CONTENT_SCHEMA["items"]
    try:
        jsonschema.validate(block, schema)
    except jsonschema.ValidationError as e:
        #print(e)
        return False
    else:
        return True

def content_is_valid(content_frag: dict):
    schema = ARTICLE_CONTENT_SCHEMA
    try:
        jsonschema.validate(content_frag, schema)
    except jsonschema.ValidationError as e:
        #print(e)
        return False
    else:
        return True