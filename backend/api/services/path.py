import os

def get_filepath(instance, filename):
    path = os.path.join(f"author_{instance.author.id}", f"article_{instance.article.id}", filename)
    return path