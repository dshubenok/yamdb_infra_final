from django.urls import path

from .views import ReviewListAPIView, ReviewDetailAPIView, CommentListAPIView, CommentDetailAPIView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListAPIView.as_view(), name='reviews_list'),
    path('<int:review_id>/', ReviewDetailAPIView.as_view(), name='reviews_detail'),

    path('<int:review_id>/comments/', CommentListAPIView.as_view(), name='comments_list'),
    path('<int:review_id>/comments/<int:comment_id>/', CommentDetailAPIView.as_view(), name='comments_detail'),
]
