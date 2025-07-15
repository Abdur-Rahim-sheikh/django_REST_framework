from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetDetail, SnippetList, UserDetail, UserList

urlpatterns = [
    path("snippets/", SnippetList.as_view(), name="snippets"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet_details"),
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
