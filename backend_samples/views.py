from django.utils.encoding import smart_str, smart_unicode
from website.models import *
from django.http import HttpResponse
from rest_framework import viewsets 
from rest.serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import authentication, permissions
import csv, json

import datetime
import os
import subprocess
from django.conf import settings

class ReportAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        
        pMsgID = request.DATA["msgID"]
        message = Post.objects.get(pk=pMsgID)
		
		# make the changes to the message
        
		
        message.save()
        
        serializer = CustomPostListSerializer(message, many=False, context={'request':request})
        return Response(serializer.data)
		
    def get(self, request, format=None):
	
		# similar to post
		
		# this will output some pre-set JSON
		
		return Response({"status": requests[0].status, "statusDT":requests[0].updateDT})
		
		
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(Q(replyLevel__exact=1))
    serializer_class = PostListSerializer
    
    def list(self, request):
		# this will be called on URL of the type www.xsfds.com/posts
        
        # get the GET params from the HTTP request
        allPosts = request.QUERY_PARAMS.get('allPosts', None)
        suicidalComments = request.QUERY_PARAMS.get('suicidalComments', None)
        forReview = request.QUERY_PARAMS.get('forReview', None)
        pageID = request.QUERY_PARAMS.get('pageID', None)
        
		# get the query set
		queryset = Post.objects.filter(Q(replyLevel__exact=1) & Q(pageID__exact=pageID)).order_by('-createdTime')

        
        serializer = PostDetailSerializer(queryset, many=True, context={'request':request})
        
		# return the serialized content of the queryset
		return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
		# This will be called on URLS of the type www.xsfds.com/posts/2/    (arg pk = 2)
	
        queryset = Post.objects.filter(Q(replyLevel__exact=1)).order_by('-createdTime')
		
        post = get_object_or_404(queryset, pk=pk)        # show a 404 not found error if the object does not exist
        
		serializer = PostDetailSerializer(post, context={'request':request})
            
        return Response(serializer.data)