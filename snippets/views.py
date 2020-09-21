from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.models import Snippet
from rest_framework import generics
from django.contrib.auth.models import User


# snippets/
class SnippetListView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.users)


# snippets/id/
class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# users/
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# users/id
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
