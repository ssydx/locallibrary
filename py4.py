import os
import django
# 设置 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
# 初始化 Django
django.setup()

from catalog.models import *
query_set = Book.objects.all()
print(query_set.db)
print(query_set.ordered)
# select * from T
query_set = Book.objects.all()
print(query_set)
# select count(*) from T
query_set = Book.objects.count()
print(query_set)
query_set = Book.objects.all()
for book in query_set:
    print(book.summary)
# select * from T where title='终极教师'
query_set = Book.objects.filter(title='终极教师')
print(query_set)
# select * from T where title='终极教师'
query_set = Book.objects.filter(title__exact='终极教师')
print(query_set)
# select * from T where title like '%天%'
query_set = Book.objects.filter(title__contains='天')
print(query_set)
# select * from T where id in [1,3,5]
query_set = Book.objects.filter(id__in=[1,3,5])
print(query_set)
# select * from T where id < 5
query_set = Book.objects.filter(id__gt=5)
print(query_set)
# select * from T where id <= 5
query_set = Book.objects.filter(id__gte=5)
print(query_set)
# select * from T where id > 5
query_set = Book.objects.filter(id__lt=5)
print(query_set)
# select * from T where id >= 5
query_set = Book.objects.filter(id__lte=5)
print(query_set)
# select * from T where title like '送%'
query_set = Book.objects.filter(title__startswith='送')
print(query_set)
# select * from T where title like '%生'
query_set = Book.objects.filter(title__endswith='生')
print(query_set)
# select * from T where id between 3 and 5(闭区间)
query_set = Book.objects.filter(id__range=(3,5))
print(query_set)
# __date,__year,__month,__day,__week,__week_day,__quarter
# __time,__hour,__minute,__second
# __isnull
# __regex=r'pattern'
# 含有i的版本为不区分大小写
# select * from T where title like '送%'
from django.db.models import Q
# select * from T where title like '%生' or id > 5
query_set = Book.objects.filter(Q(title__endswith='生') | Q(id__gt=5))
print(query_set)
# select * from T where title like '%生' or id > 5
query_set = Book.objects.filter(title__endswith='生') | Book.objects.filter(id__gt=5)
print(query_set)
# select * from T where title like '%生' and id < 5
query_set = Book.objects.filter(title__endswith='生').filter(id__lt=5)
print(query_set)
# select * from T where title not like '%生'
query_set = Book.objects.exclude(title__endswith='生')
print(query_set)
# select * from T where title not like '%生' and not id < 5
query_set = Book.objects.exclude(title__endswith='生').exclude(id__lt=5)
print(query_set)
# select * from T where not (title like '%生' and id < 5)
query_set = Book.objects.exclude(title__endswith='生', id__lt=5)
print(query_set)
print('--------------------------------------')
from django.db.models import Count
q = Author.objects.annotate(Count('book'))
print(q[0].first_name)
print(q[0].book__count)
q = Author.objects.annotate(bookcnt=Count("book"))
print(q[2].first_name)
print(q[2].bookcnt)
q = Author.objects.alias(bookcnt=Count("book")).filter(bookcnt__gt=3)
print(q[0].first_name)

# 表的ordering
query_set = Book.objects.all()
print(query_set)
query_set = Book.objects.order_by('-id')
print(query_set)
# author外键默认按外键所在表的ordering排序，没有则按主键排序，想按外键表的某字段排序需显式指定
query_set = Book.objects.order_by('author','-id')
print(query_set)
# 等价于
query_set = Book.objects.order_by('author__last_name','author__first_name','-id')
print(query_set)
# 强制按外键主键排序
query_set = Book.objects.order_by('author__id','-id')
print(query_set)
# 以下方式为什么也能按主键排序？？？
# query_set = Book.objects.order_by('author_id','-id')
# print(query_set)
# 反转原ordering（没有则按主键）顺序
query_set = Book.objects.reverse()
print(query_set)
# 只有这种无参的可以应用在MySQL和SQLite，有参的只能用于PostgreSQL
query_set = Book.objects.distinct()
print(query_set)
# 返回模型实例列表（每一项都是模型实例，模型实例就是以__str__定义的名称为变量名称varname的一条数据记录，queryset中以<ModelName: varname>显示）
query_set = Author.objects.all()
print(query_set)
# 返回字典列表（每一项都是字典，形如：{'fieldname':field1value,'fieldname':field1value,'fieldname':field1value}）
query_set = Author.objects.values()
print(query_set)
# 返回指定字段
query_set = Author.objects.values('id','last_name','first_name')
print(query_set)
# 计算字段
from django.db.models.functions import Concat
query_set = Author.objects.values('id',name=Concat('last_name','first_name'))
print(query_set)
# 从中不难看到，queryset中的外键名实际是field_id
query_set = Book.objects.values()[0]
print(query_set)
query_set = Book.objects.values('author')[0]
print(query_set)
query_set = Book.objects.values('author_id')[0]
print(query_set)


query_set = Book.objects.values()[0]
print(query_set)
# values_list是元组，取自字典中的键值对中的值
query_set = Book.objects.values_list()[0]
print(query_set)
# values_list指定单个值的话可以使用flat参数将单元素元组转为单值
query_set = Book.objects.values_list('title',flat=True)
print(query_set)
# 多值则可以使用named参数，使其成为RAW(fieldname=fieldvalue,fieldname=fieldvalue)的元组形式
query_set = Book.objects.values_list('title','isbn',named=True)
print(query_set)

query_set = Author.objects.dates('date_of_birth','year')
print(query_set)
query_set = Author.objects.dates('date_of_birth','month')
print(query_set)
query_set = Author.objects.dates('date_of_birth','week')
print(query_set)
query_set = Author.objects.dates('date_of_birth','day')
print(query_set)
query_set = Author.objects.dates('date_of_birth','day',order='DESC')
print(query_set)
# datetimes同理
# 空查询集
query_set = Author.objects.none()
print(query_set)

# q1.union(q2,q3...,all=False|True)
# q1.intersection(q2,q3...)
# q1.diffrerence(q2,q3...)

import time

starttime1 = time.perf_counter()
query_set = Book.objects
for i in range(1,1):
    q1 = query_set.values('title','author__last_name')
    print(q1)
    q2 = query_set.values('title','author__first_name')
    print(q2)
    q3 = query_set.values('title','author__date_of_birth')
    print(q3)
    q4 = query_set.values('title','author__date_of_death')
    print(q4)
    q5 = query_set.values('title','author__gender')
    print(q5)
    q1 = query_set.values('title','author__last_name')
    print(q1)
    q2 = query_set.values('title','author__first_name')
    print(q2)
    q3 = query_set.values('title','author__date_of_birth')
    print(q3)
    q4 = query_set.values('title','author__date_of_death')
    print(q4)
    q5 = query_set.values('title','author__gender')
    print(q5)
endtime1 = time.perf_counter()
print(endtime1-starttime1)
# 它与直接查询的区别在于此时author表同book表都被从数据库取出,多次获取外键所在表的值不会反复进数据库寻找外键所在表
starttime2 = time.perf_counter()
query_set = Book.objects.select_related('author')
for i in range(1,1):
    q1 = query_set.values('title','author__last_name')
    print(q1)
    q2 = query_set.values('title','author__first_name')
    print(q2)
    q3 = query_set.values('title','author__date_of_birth')
    print(q3)
    q4 = query_set.values('title','author__date_of_death')
    print(q4)
    q5 = query_set.values('title','author__gender')
    print(q5)
    q1 = query_set.values('title','author__last_name')
    print(q1)
    q2 = query_set.values('title','author__first_name')
    print(q2)
    q3 = query_set.values('title','author__date_of_birth')
    print(q3)
    q4 = query_set.values('title','author__date_of_death')
    print(q4)
    q5 = query_set.values('title','author__gender')
    print(q5)
endtime2 = time.perf_counter()
print(endtime2-starttime2)

query_set = Author.objects.raw(
    '''
    select id,last_name || first_name as name
    from catalog_author
    '''
)
print(query_set)
for author in query_set:
    print(f"ID: {author.id}, Name: {author.name}")


query_set = Book.objects.values().get(id=1)
print(query_set)
# 不进行字段约束的验证，到底验证不验证
# query_set = Book.objects.bulk_create([Book(title='剑风传奇')])
# print(query_set)
# 不进行字段约束的验证，到底验证不验证
# query_set = Book.objects.create(title='星际牛仔',isbn='8659745698758')
# print(query_set)
# 不知道有什么意义
# query_set = Book.objects.in_bulk(['9787540336677','9787574900141'], field_name='isbn')
# print(query_set)

query_set = Author.objects.values('id','last_name','first_name').explain()
print(query_set)


