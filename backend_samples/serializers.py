from rest_framework import serializers
from website.models import *

class CustomPostListSerializer(serializers.HyperlinkedModelSerializer):

    replies = ReplyNestedContentSerializer(many=True)
    class Meta:
        model = Post 
        fields = ("url", 'msgID', 'msgText', 'msgAuthor', 'msgAuthorID', 'msgAuthorProfilePic', 'msgLikes', 'createdTime', 'commentCount', 'suicideDetectionLabel', 'toDisplay', 'topics', 'replies')



class ReplyNestedContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ("url", 'msgID', 'msgText', 'msgAuthor', 'msgAuthorID', 'msgAuthorProfilePic', 'msgLikes', 'createdTime', 'commentCount', 'suicideDetectionLabel', 'toDisplay')
        
		
class PageDetailSerializer(serializers.HyperlinkedModelSerializer):
    topics = serializers.HyperlinkedRelatedField(
        view_name="topic-detail",
        many=True
    )
    
    class Meta:
        model = Page 
        fields = ('pageName', 'insertTime', 'topics')