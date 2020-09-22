from snippets.views import SnippetDetailView, SnippetListView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetListView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/',
         SnippetDetailView.as_view(),
         name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
