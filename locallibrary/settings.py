from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kb6_#6w#ug^u_1_whrwn@wpa^*25a3&4e7nl=r03vly4qyv062'
WSGI_APPLICATION = 'locallibrary.wsgi.application'

# 基准目录配置
BASE_DIR = Path(__file__).resolve().parent.parent
# 网址配置：此处为使用locallibrary目录下的url.py
ROOT_URLCONF = 'locallibrary.urls'
# 允许页面错误时显示错误详情
DEBUG = True


# import os
# import sys
# MY_APP_PATH = os.path.join(BASE_DIR, '../base_test/field')
# MY_APP_PATH = os.path.normpath(MY_APP_PATH)
# if MY_APP_PATH not in sys.path:
#     sys.path.insert(0, MY_APP_PATH)
# print(sys.path)


# 允许的主机
ALLOWED_HOSTS = [
    'example.com',
    'www.example.com',
    '127.0.0.1',  # 本地开发环境
    'localhost',  # 本地开发环境
    '192.168.1.3',
]
# Application definition
# 应用程序配置

INSTALLED_APPS = [
    # 管理模块
    'django.contrib.admin',
    # 验证模块
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 会话模块
    'django.contrib.sessions',
    'django.contrib.messages',
    # 静态文件收集器模块
    'django.contrib.staticfiles',
    # 个人应用模块
    'catalog.apps.CatalogConfig',
    'blog.apps.BlogConfig'
    # 'field',
]
# 中间件配置
MIDDLEWARE = [
    # 安全中间件
    'django.middleware.security.SecurityMiddleware',
    # 会话中间件
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 普通中间件
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 验证中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 消息中间件
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 模板引擎配置
TEMPLATES = [
    # 引擎其一，可以设置更多引擎，但通常不必要
    # 如果设置了多个引擎，默认会使用列表中的第一个引擎
    # 如果想在视图中使用其他引擎请在视图中指定，详情百度
    {
        # 引擎名称
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 模板目录，即工程项目下的templates目录
        'DIRS': ['templates',],
        # 是否在应用程序下的templates目录查找
        'APP_DIRS': True,
        # 额外选项
        'OPTIONS': {
            # 上下文处理器列表
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 数据库配置
DATABASES = {
    # 如果想同时使用多个数据库，请百度
    # 数据库其一，默认数据库
    'default': {
        # 数据库引擎
        'ENGINE': 'django.db.backends.sqlite3',
        # 数据库名称
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mysql': {
        # 引擎名称
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名称，事先已创建
        'NAME': 'django_db',
        'USER': 'ssydx',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}
# 密码验证器配置
AUTH_PASSWORD_VALIDATORS = [
    # 密码与用户名相似
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # 密码最小长度
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # 普通密码验证器
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # 纯数字密码
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 语言设置（非模板显示的内容）
LANGUAGE_CODE = 'zh-hans'
# 时区设置
TIME_ZONE = 'Asia/Shanghai'
# 启用国际化
USE_I18N = True
# 启用时区感知
USE_TZ = True

# 不知道为什么不对
# 静态文件基准目录
STATIC_URL = '/static/'
# import os
# STATIC_ROOT = os.path.join(BASE_DIR, 'catalog/static')

# 默认主键的字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# 登录后重定向
LOGIN_REDIRECT_URL = '/'
# 邮件转接至控制台
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

