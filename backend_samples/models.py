from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User


# a post on the page's feed
#
class Post(models.Model):
  msgID = models.CharField(max_length=128, primary_key=True, unique=True, db_index=True, editable=False)		# unique identifier assigned by Facebook: the primary DB key
  replyLevel = models.PositiveSmallIntegerField(db_index=True, editable=False)  # was this a post, comment, or reply?
  msgText = models.TextField()                  # the actual message
  msgAuthor = models.CharField(max_length=128)	# name of the author
  msgAuthorID = models.CharField(max_length=32)	# unique identifier of author, assigned by Facebook
  msgAuthorProfilePic = models.CharField(max_length=192)	# URL to author's profile pic
  msgLikes = models.PositiveIntegerField()	# number of "likes"
  repliedTo = models.ForeignKey('self', null=True, related_name='replies')	# post to which this message responded
  createdTime = models.DateTimeField()	# date/time of message creation (Python datetime.datetime instance)
  insertTime = models.DateTimeField(auto_now_add=True)	# date/time when message was first added to our app (Python datetime.datetime instance)
  updateTime = models.DateTimeField(auto_now=True, null=True)	# date/time when this record is updated
  commentCount = models.IntegerField(default=0)  # number of comments or replies, if applicable
  topics = models.ManyToManyField(Topic, null=True, default=None, related_name='posts') # topics assigned to this post
  suicideDetectionLabel = models.IntegerField(default=0)  # 0 = unlabeled, 1 = REPORT, 2 = FALSE ALARM
  pageID = models.ForeignKey(Page, related_name='posts')	# ID of the page. 
  toDisplay = models.BooleanField(default=True)
  toBeReviewed = models.BooleanField(default=False)
  usefulSuggestionLabel = models.IntegerField(default=0)  # 0 = unlabeled, 1 = USEFUL, 2 = NOT USEFUL
  
  def all(self):
      return Post.objects.filter(toDisplay__exact=True)