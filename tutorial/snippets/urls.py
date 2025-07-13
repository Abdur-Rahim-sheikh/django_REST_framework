from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetDetail, SnippetList

urlpatterns = [
    path("snippets/", SnippetList.as_view(), name="snippets"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
