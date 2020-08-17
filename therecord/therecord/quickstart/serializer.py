from rest_framework import serializers

from quickstart.models import Item

class ItemSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Item
        fields = ('id', 'title', 'date_published', 'url', 'content_html')