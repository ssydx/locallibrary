import os
import django
# 设置 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
# 初始化 Django
django.setup()


from catalog.models import Author

for e in Author.objects.all():
    print(e.gender)
print(Author)
print(Author.objects)
print(Author.objects.all())
print(list(Author.objects.all()))
