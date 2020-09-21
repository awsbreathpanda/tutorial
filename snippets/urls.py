from django.urls import path
from snippets.views import SnippetListView, SnippetDetailView, UserDetailView, UserListView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetListView.as_view()),
    path('snippets/<int:pk>/', SnippetDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
