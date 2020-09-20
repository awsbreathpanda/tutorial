from django.urls import path
from snippets.views import SnippetListView, SnippetDetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetListView.as_view()),
    path('snippets/<int:pk>/', SnippetDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
