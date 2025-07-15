from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CommentPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)

CommentPaginator = CommentPagination()