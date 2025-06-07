from api.models import CustomUser
from rest_framework.request import Request
from rest_framework.response import Response

def check_ownership(obj, user: CustomUser):
    if obj.user == user:
        return True
    else:
        return False
    
def ownership_required(model=None):
    def _view_wrapper(view):
        def _wrapped_view(self, request: Request, id: int, *args, **kwargs):
            user = request.user 
            if model:
                sel_obj = model.objects.get(pk=id)
            else:
                sel_obj = self.queryset.get(pk=id)

            if not check_ownership(sel_obj, user):
                return Response({"message": "This resource is owned by a different user!"}, status=401)
            else:
                return view(self, request, id, sel_obj=sel_obj, *args, **kwargs)
        return _wrapped_view
    return _view_wrapper 
        