from django.http import HttpResponseNotFound
from rest_framework.response import Response


def custom_404_view(request, exception=None):
    return Response({"message": 'Resource not found!'}, status=404)