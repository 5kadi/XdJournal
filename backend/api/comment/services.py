from .models import Comment

def get_user_related_data(request_user, comment_obj: Comment):
    data = {
        "is_owner": False,
        "is_liked": False
    }
    data["is_owner"] = request_user == comment_obj.user
    if data["is_owner"]:
        data["is_liked"] = bool(comment_obj.api_commentlike.filter(user=request_user).count())

    return data