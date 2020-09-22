from django.urls import path
from snippets.views import SnippetListView, SnippetDetailView, api_root, SnippetHighlight
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetListView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/',
         SnippetDetailView.as_view(),
         name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
         SnippetHighlight.as_view(),
         name='snippet-highlight'),
    path('', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
