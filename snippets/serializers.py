from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # model中的外键必须在serializer中这样处理一下
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:

        model = Snippet
        fields = '__all__'
