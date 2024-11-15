import os
import django
# 设置 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
# 初始化 Django
django.setup()


from django.contrib.sessions.models import Session
from django.utils import timezone

# 获取当前有效的所有会话
sessions = Session.objects.filter(expire_date__gt=timezone.now())
for session in sessions:
    data = session.get_decoded()
    print(data)