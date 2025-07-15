from .models import ArticleLike, CommentLike
from api.serializers import ReadOnlyModelSerializer
from api.article.serializers import ArticleListSerializer
from api.comment.serializers import CommentListSerializer

#foreshadowing
class ArticleLikeListSerializer(ReadOnlyModelSerializer):
    article = ArticleListSerializer()
    class Meta:
        model = ArticleLike
        fields = ["article"]

class CommentLikeListSerializer(ReadOnlyModelSerializer):
    comment = CommentListSerializer()
    class Meta:
        model = CommentLike
        fields = ["comment"]