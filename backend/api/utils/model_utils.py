import os
import jsonschema

def get_filepath(instance, filename):
    path = os.path.join(f"author_{instance.author.id}", f"article_{instance.article.id}", filename)
    return path


def generate_frag_id():
    import uuid 
    return str(uuid.uuid4().fields[-1])[:5]

def default_content():
    return {
        generate_frag_id(): {
            "type": "text", 
            "content": "Express yourself here!"
        }
    }



