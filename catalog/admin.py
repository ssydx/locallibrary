from django.contrib import admin


from .models import Author, Genre, Book, BookInstance, Language


admin.site.register(Genre)
admin.site.register(Language)

# 创建内联模型（即在某表的详情页嵌入另一个表）
class BooksInstanceInline(admin.TabularInline):
    # 被嵌入的表为书籍状态表
    model = BookInstance
    # 除原有记录外的额外空记录数
    extra = 1
class BooksInline(admin.StackedInline):
    # 被嵌入的表为书籍状态表
    model = Book
    # 除原有记录外的额外空记录数
    extra = 1
    min_num = 1
    max_num = 2
    can_delete = False
    show_change_link = True
    fields = [
        ('title', 'isbn'), 
        'summary', 
    ]



class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'last_name', 
        'first_name', 
        'gender', 
        'get_birthAnddeath', 
    ]
    list_display_links = [
        '__str__',
        'first_name', 
        'last_name', 
    ]
    list_editable = [
        'gender', 
    ]
    list_filter = [
        'last_name', 
        'date_of_death', 
    ]
    list_max_show_all = 10
    list_per_page = 3

    ordering = ['last_name', ]
    search_fields = ['first_name', 'last_name', ]
    search_help_text = '在姓氏和名字两个字段搜索'

    readonly_fields = ['date_of_birth', ]

    fields = [
        ('last_name', 'first_name', ), 
        ('date_of_birth', 'date_of_death', ), 
        'gender', 
    ]

    save_on_top = True
    save_as = True
    save_as_continue = False
    view_on_site = False
    date_hierarchy = 'date_of_birth'
    inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    filter_horizontal = ['genre']
    # 在书籍表中嵌入书籍状态表的内联模型
    inlines = [BooksInstanceInline]



@admin.action(
    description="更新所选的 %(verbose_name_plural)s 的imprint字段为123"
)
def set_imprint(modeladmin, request, queryset):
    # 将选集中的记录的imprint字段统一更新为123
    queryset.update(imprint="123")

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', )
    # 添加过滤器
    list_filter = ('status', 'due_back')
    readonly_fields = ['id', ]
    # 详情界面分组，两个分组，第一分组无组名，第二分组组名为'Availability'
    fieldsets = (
        (None, {
            'fields': ('book','imprint','id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    show_full_result_count = False
    # 增加动作，用于批量操作
    actions = [set_imprint, ]

