"""관계 객체를 읽는 ORM 쿼리 수를 비교하는 함수 모음이다."""
from django.db import connection
from django.db.models import Count
from django.test.utils import CaptureQueriesContext

from .models import Post


def _measure(queryset, row_builder):
    # QuerySet 평가와 관계 접근을 캡처 구간 안에서 함께 실행한다.
    with CaptureQueriesContext(connection) as captured:
        rows = [row_builder(post) for post in queryset]
    return {"rows": rows, "query_count": len(captured)}


def compare_author_queries():
    """작성자 접근의 N+1 쿼리와 select_related 결과를 비교한다."""
    plain = _measure(
        Post.objects.order_by("pk")[:3],
        lambda post: (post.pk, post.title, post.author.name),
    )
    optimized = _measure(
        Post.objects.select_related("author").order_by("pk")[:3],
        lambda post: (post.pk, post.title, post.author.name),
    )
    return {"plain": plain, "optimized": optimized}


def compare_comment_queries():
    """역참조 댓글 접근의 N+1 쿼리와 prefetch_related 결과를 비교한다."""
    plain = _measure(
        Post.objects.order_by("pk")[:3],
        lambda post: (post.pk, post.title, [comment.content for comment in post.comments.all()]),
    )
    optimized = _measure(
        Post.objects.prefetch_related("comments").order_by("pk")[:3],
        # all()은 prefetch_related가 채운 역참조 캐시를 사용한다.
        lambda post: (post.pk, post.title, [comment.content for comment in post.comments.all()]),
    )
    return {"plain": plain, "optimized": optimized}


def show_comment_counts():
    """Count 집계로 게시글별 댓글 수를 한 번의 쿼리로 읽는다."""
    with CaptureQueriesContext(connection) as captured:
        rows = [(post.title, post.comment_count) for post in (
            Post.objects.annotate(comment_count=Count("comments")).order_by("pk")[:3]
        )]
    return {"rows": rows, "query_count": len(captured)}