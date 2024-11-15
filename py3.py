import os
import django
# 设置 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
# 初始化 Django
django.setup()


from catalog.views import get_date_time

res = get_date_time()
res.headers['age']=20
print(res)
print(res.headers)
print(res.write('123'))
print(res.getvalue())
