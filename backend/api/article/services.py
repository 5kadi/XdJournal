from .models import ARTICLE_CONTENT_SCHEMA, Article
import jsonschema
import re


def article_list(*args, **kwargs):
    data = Article.objects.all()
    return data

#insert & pop

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

#content related
def make_safe(content: str) -> str:
    GENERAL_PATTERN = r"<(.+)(?: \w+(?:=\"[^\"]*\")*)*>([^<>]*)</\1>"
    SAFE_PATTERN = r'<span class=\"[^\"]+\">[^<>]*</span>'

    def _repl(match: re.Match) -> str:
        start, end = match.span()
        substr = match.string[start:end]
        if re.match(SAFE_PATTERN, substr):
            return substr
        else:
            return match.group(2) #([^<>]*) in GENERAL_PATTERN
    
    return re.sub(GENERAL_PATTERN, _repl, content)
    
def modify_content(article_obj: Article, block_id: int, block: dict): #its ensured that object exists
    """Modify content of block by its id"""
    article_content: list = article_obj.content
    if block_id < len(article_content):
        article_content[block_id] = block
    else:
        article_content.append(block)
    article_obj.save()

"""
def modify_content_s(article_obj: Article, block_id: int, block: dict):
    block["content"] = make_safe(block["content"])
    modify_content(article_obj, block_id, block)
"""

def block_is_valid(block: dict):
    schema = ARTICLE_CONTENT_SCHEMA["items"]
    try:
        jsonschema.validate(block, schema)
    except jsonschema.ValidationError as e:
        #print(e)
        return False
    else:
        return True
