from django.urls import path
from catalog import views
# 将应用程序根目录托管给指定视图
urlpatterns = [
    path('', views.index, name='index'),
]
# 列表视图
urlpatterns += [
    path('books/', views.BookListView.as_view(), name='books'),
]
urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
]
# 详情视图
urlpatterns += [
    path('book/<int:pk>', views.BookDetailView.as_view(), name='bookdetail'),
]
urlpatterns += [
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='authordetail'),
]
# 混合视图
urlpatterns += [
    path('mybooks/', views.UserBorrowedView.as_view(), name='myborrowed'),
]
urlpatterns += [
    path('allbooks/', views.AllBorrowedView.as_view(), name='allborrowed'),
]
# 表单视图
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
# 编辑视图
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]



urlpatterns += [
    path('testform/', views.testview, name='testform'),
]
urlpatterns += [
    path('test0/', views.get_date_time, name='datetime')
]
from django.views.generic import TemplateView
urlpatterns += [
    path('test1/', TemplateView.as_view(template_name='test/1.html'))
]
urlpatterns += [
    path('test2/', views.AboutView.as_view())
]
urlpatterns += [
    path('test3/', views.AboutFunc)
]