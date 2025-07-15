from django.urls import path, include
from .views import ArticleView

urlpatterns = [
    path(r"get/<int:id>", ArticleView.as_view({'get': 'get'})),
    path(r"list", ArticleView.as_view({'get': 'list'})),
    path(r"create", ArticleView.as_view({'post': 'create'})),
    path(r"<int:id>/save_block", ArticleView.as_view({'patch': 'save_block'})),
    path(r"<int:id>/delete_block", ArticleView.as_view({'patch': 'delete_block'})),
    path(r"<int:id>/reposition_block", ArticleView.as_view({'patch': 'reposition_block'})),
    path(r"<int:id>/publish", ArticleView.as_view({'patch': 'publish'})),
]