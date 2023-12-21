from django.urls import path, re_path
from blog import views

app_name = 'blog'
url_patterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('/about',views.AboutView.as_view(),name="about"),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new',views.PostCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove',views.PostDeleteView,name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/delete',views.comment_remove,'comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,'post_publish')
]