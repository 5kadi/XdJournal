from .models import ARTICLE_CONTENT_SCHEMA, Article
import jsonschema
import re


class ArticleBlockError(Exception): ...

class ArticleBlockService:
    def __init__(self, article_obj: Article):
        self.article_obj = article_obj
        self.article_content: list[dict] = article_obj.content

    @staticmethod
    def purify_content(content: str) -> str:
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
    
    @staticmethod
    def is_valid_block(block: dict):
        schema = ARTICLE_CONTENT_SCHEMA["items"]
        try:
            jsonschema.validate(block, schema)
        except jsonschema.ValidationError as e:
            #print(e)
            return False
        else:
            return True
        
    def modify_block(self, block_id: int, block: dict):
        if block_id < len(self.article_content):
            self.article_content[block_id] = block
        else:
            self.article_content.append(block)
        self.article_obj.save()

    def insert_block(self, block_id: int, block: dict):
        if block_id < len(self.article_content):
            self.article_content.insert(block_id, block)
        else:
            self.article_content.append(block)
        self.article_obj.save()

    def pop_block(self, block_id: int) -> dict:
        if len(self.article_content) > 1:
            block = self.article_content.pop(block_id)
            self.article_obj.save()
            return block
        else:
            raise ArticleBlockError("Article must have at least 1 block!")

    """   
    def swap_block(self, initial_pos: int, final_pos: int):
        if any([
            initial_pos >= len(self.article_content),
            final_pos >= len(self.article_content),
            initial_pos < 0,
            final_pos < 0
        ]):
            raise ArticleBlockError("Incorrect positions!")

        temp = self.article_content[initial_pos]
        self.article_content[initial_pos] = self.article_content[final_pos]
        self.article_content[final_pos] = temp

        print(self.article_content)

        self.article_obj.save()
    """


def get_user_related_data(request_user, article_obj: Article):
    data = {
        "is_owner": False,
        "is_liked": False
    }
    data["is_owner"] = request_user == article_obj.user
    if data["is_owner"]:
        data["is_liked"] = bool(article_obj.api_articlelike.filter(user=request_user).count())

    return data
