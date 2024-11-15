from django.db import models

from django.urls import reverse
import uuid
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
# 载入内置的用户表
from django.contrib.auth.models import User
from datetime import date
from django.contrib import admin

# 书籍类型表
class Genre(models.Model):
    name = models.CharField(
        verbose_name='类型名称',
        help_text='输入一个书籍类型，例如科幻小说、网络小说',
        max_length=100,
        unique=True,
    )
    class Meta:
        verbose_name = '书籍类型'
        verbose_name_plural = '书籍类型表'
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='类型名称唯一约束',
                violation_error_message = "类型已存在（不区分大小写）"
            )
        ]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('genredetail', args=[str(self.id)])

# 书籍语言表
class Language(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text='输入一个书籍语言，例如中文、日语',
        verbose_name='语言名称',
    )
    class Meta:
        verbose_name = '书籍语言'
        verbose_name_plural = '书籍语言表'    
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='语言名称唯一约束',
                violation_error_message = "语言已存在（不区分大小写）"
            )
        ]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('languagedetail', args=[str(self.id)])

# 书籍作者表
class Author(models.Model):
    first_name = models.CharField(
        max_length=100, 
        verbose_name='名',
    )
    last_name = models.CharField(
        max_length=100, 
        verbose_name='姓',
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True, 
        verbose_name='出生日期',
    )
    date_of_death = models.DateField(
        '去世日期', 
        null=True, 
        blank=True
    )
    SEX = [
        ('M', '男'),
        ('F', '女'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=SEX,
        default='M', 
        verbose_name='性别'
    )
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = '书籍作者'
        verbose_name_plural = '书籍作者表'
    def __str__(self):
        gender_display = dict(self.SEX).get(self.gender, '')
        return f'{self.last_name}{self.first_name} ({gender_display})'
    def get_absolute_url(self):
        return reverse('authordetail', args=[str(self.id)])
    # 用于管理员站点的列表显示
    @admin.display(description='生卒信息')
    def get_birthAnddeath(self):
        return f'{self.date_of_birth}至{self.date_of_death}'

# 书籍表
class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='书籍标题',
    )
    summary = models.TextField(
        max_length=1000,
        verbose_name='书籍简介',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.RESTRICT,
        null=True,
        verbose_name='书籍作者',
    )
    language = models.ForeignKey(
        Language, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='书籍语言',
    )
    isbn = models.CharField(
        '书籍ISBN',
        max_length=13,
        unique=True,
        help_text='13位<a href="https://www.isbn-international.org/content/what-isbn">ISBN码</a>',
    )
    genre = models.ManyToManyField(
        Genre,
        help_text='为书籍选择一个类型',
        verbose_name='书籍类型',
    )
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍表'
        ordering = ['title', 'author']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('bookdetail', args=[str(self.id)])
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    # 与@admin.display(description='书籍类型')这个装饰器的效果完全相同
    display_genre.short_description = '书籍类型'


# 书籍状态表
class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='唯一ID用于表示每本书',
        verbose_name='书籍编号',
    )
    book = models.ForeignKey(
        'Book',
        on_delete=models.RESTRICT,
        null=True,
        verbose_name='书籍'
    )
    imprint = models.CharField(max_length=200,verbose_name='书籍Imprint')
    due_back = models.DateField(null=True, blank=True,verbose_name='归还日期')
    # 外键引用User表的主键
    borrower = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='借阅者')
    # 该装饰器用于将方法转化为属性来使用，仅适用于不接受外部参数的情况
    @property
    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)
    LOAN_STAUS = (
        ('m', '维护'),
        ('o', '借出'),
        ('a', '空闲'),
        ('r', '预定'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STAUS,
        blank=True,
        default='m',
        verbose_name='书籍状态'
    )
    class Meta:
        verbose_name = '书籍状态'
        verbose_name_plural = '书籍状态表'
        ordering = ['due_back']
        permissions = (("can_mark_returned", "return_book"),)
    def __str__(self):
        return f'{self.id} ({self.book.title})'
    def get_absolute_url(self):
        return reverse('bookinstance-detail', args=[str(self.id)])   



    