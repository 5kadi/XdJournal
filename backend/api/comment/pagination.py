from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CommentPagination(PageNumberPagination):
    page_size = 10

CommentPaginator = CommentPagination()