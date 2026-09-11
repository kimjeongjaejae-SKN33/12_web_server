from django.urls import path

from . import views_fbv
from .views_cbv import PostCreateView, PostDetailView, PostListView

app_name = "board"

urlpatterns = [
    path("", views_fbv.post_list, name="home"),
    path("fbv/", views_fbv.post_list, name="fbv_list"),
    path("fbv/<int:pk>/", views_fbv.post_detail, name="fbv_detail"),
    path("cbv/", PostListView.as_view(), name="cbv_list"),
    path("cbv/new/", PostCreateView.as_view(), name="cbv_create"),
    path("cbv/<int:pk>/", PostDetailView.as_view(), name="cbv_detail"),
]