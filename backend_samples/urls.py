from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest import views

router.register(r'post', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^report/', views.ReportAPIView.as_view(), name="report"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)