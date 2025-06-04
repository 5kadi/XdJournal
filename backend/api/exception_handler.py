from django.http import Http404
from rest_framework.views import exception_handler, set_rollback
from rest_framework.exceptions import NotFound, PermissionDenied, APIException
from rest_framework.response import Response


def custom_exception_handler(exc, context):

    if isinstance(exc, Http404):
        exc = NotFound(*(exc.args))
    elif isinstance(exc, PermissionDenied):
        exc = PermissionDenied(*(exc.args))

    if isinstance(exc, APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'message': exc.detail} #changed line

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None