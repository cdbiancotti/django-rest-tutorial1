from rest_framework import fields, serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # Can use ChartField(read_only=True) instead of ReadOnlyField
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'title', 'code', 'linenos',
                  'language', 'style', 'owner']
