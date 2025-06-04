from django.db import models
from django.contrib import auth
from django.utils import timezone
import uuid 

def default_content():
    
    return {
        str(uuid.uuid4().fields[-1])[:5]: {
            "type": "text", 
            "content": "Express yourself here!"
        }
    }

ARTICLE_CONTENT_SCHEMA = {
        "type": "object",
        "patternProperties": {
                r"^[A-Za-z0-9]+": {
                "type": "object", 
                "properties": {
                    "type": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["type", "content"],
                "additionalProperties": False
            }
        }
    } 

class Article(models.Model):
    user = models.ForeignKey(to=auth.get_user_model(), on_delete=models.CASCADE, related_name='articles') #creator (User)
    create_date = models.DateTimeField(db_index=True, default=timezone.now) #creation date
    update_date = models.DateTimeField(auto_now=True) #last update date
    header = models.CharField(max_length=100, default="Unnamed article")
    content = models.JSONField(default=default_content) #article text (XdMD)
    is_published = models.BooleanField(default=False) 

    #@property
    #def related_media(self):
        #return self.media.all()