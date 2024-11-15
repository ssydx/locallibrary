from django.shortcuts import render
from .models import *
from .forms import *
# 视图函数
def index(request):
    # 书籍表的记录数
    num_books=Book.objects.all().count()
    # 书籍状态表的记录数
    num_instances=BookInstance.objects.all().count()
    # 书籍状态表中状态为可获得的记录数
    num_instances_maitainance=BookInstance.objects.filter(status__exact='m').count()
    # 作者表的记录数
    num_authors=Author.objects.count()
    # 类型表中名称包含'小说'的记录数
    num_genre_filter=Genre.objects.filter(name__contains='小说').count()
    # 记录访问次数
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    # 将变量注入索引页的上下文
    return render(
        request,
        'catalog/index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_maitainance':num_instances_maitainance,
            'num_authors':num_authors,
            'num_genre_filter':num_genre_filter,
            'num_visits':num_visits,
            }
    )

from django.views import generic
# 列表视图
class BookListView(generic.ListView):
    model = Book
    # 上下文对象名，默认为modelname_list
    context_object_name = 'books'
    # 基于catalog/templates/的模板路径，即上下文对象注入的页面
    template_name = 'catalog/booklist.html'
    # 分页，每页项目数
    paginate_by = 5
class AuthorListView(generic.ListView):
    model = Author
    # 上下文对象名，默认为modelname_list
    context_object_name = 'authors'
    # 基于catalog/templates/的模板路径，即上下文对象注入的页面
    template_name = 'catalog/authorlist.html'
    # 分页，每页项目数
    paginate_by = 10
# 混合视图
class BookDetailView(generic.DetailView):
    model = Book
    # 默认名为modelname，即此处可不显式指定
    context_object_name = 'book'
class AuthorDetailView(generic.DetailView):
    model = Author
    # 默认名为modelname，即此处可不显式指定
    context_object_name = 'author'

# 混合视图
from django.contrib.auth.mixins import LoginRequiredMixin
class UserBorrowedView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name ='catalog/myborrowed.html'
    context_object_name = 'bookinstances'
    paginate_by = 5
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
class AllBorrowedView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name ='catalog/allborrowed.html'
    context_object_name = 'bookinstances'
    paginate_by = 10

# 表单视图
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstance, pk = pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse('allborrowed') )
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
    return render(request, 'catalog/bookrenew.html', {'form': form, 'bookinst':book_inst})

# 编辑视图
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author
class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'2018-12-12',}
    template_name = 'catalog/author_form.html'
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    template_name = 'catalog/author_form.html'
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    template_name = 'catalog/author_confirm_delete.html'
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    initial = {
        'title':'书籍标题',
    }
    template_name = 'catalog/book_form.html'
class BookUpdate(UpdateView):
    model = Book
    fields = ['title','summary']
    template_name = 'catalog/book_form.html'
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    template_name = 'catalog/book_confirm_delete.html'













def testview(request):
    form = TestForm()
    return render(
        request, 
        'catalog/form.html',
        context={
            'form': form,
        }
    )




from django.http import HttpResponse
import datetime
def get_date_time(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html, content_type='text/plain')
import random
class AboutView(generic.TemplateView):
    template_name = 'test/2.html'
    extra_context = {'number': random.randrange(1, 100)}
def AboutFunc(request):
    extra_context = random.randrange(101, 200)
    return render(
        request,
        'test/3.html',
        context={
            'number':extra_context
        }
    )
