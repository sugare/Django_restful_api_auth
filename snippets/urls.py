from django.conf.urls import url, include
from snippets.views import SnippetList, SnippetDetail, UserList, UserDetail
from snippets.views import SnippetHighlight, api_root
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(),name='snippet-detail'),
    url(r'^users/$', UserList.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(),name='user-detail'),
    url(r'^$', api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(),name='snippet-highlight'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)