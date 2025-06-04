from api.models import CustomUser
from django.db.models import Model

def check_ownership(obj: Model, user: CustomUser):
    if obj.user == user:
        return True
    else:
        return False