from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += [
    path('blogauthors/', BlogAuthorsView.as_view(), name='blogauthors'),
]
urlpatterns += [
    path('blogcontents/', BlogContentsView.as_view(), name='blogcontents'),
]
urlpatterns += [
    path('blogauthor/<int:pk>', BlogAuthorView.as_view(), name='blogauthor'),
]
urlpatterns += [
    path('blogcontent/<int:pk>', BlogContentView.as_view(), name='blogcontent'),
]