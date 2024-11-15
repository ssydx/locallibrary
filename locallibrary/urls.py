from django.urls import path

# 将工程项目根目录托管给指定视图，此处托管给指定应用程序
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='catalog/')),
]
# 将管理员目录托管给admin.site.urls的URL模式列表
# admin.site.urls：
# admin.site获得一个实例化的AdminSite对象，
# 进而获得site对象的urls属性，
# urls属性的值是模式集(元组)：(URL模式列表, app_name, namespace)
from django.contrib import admin
urlpatterns += [
    path('admin/', admin.site.urls),
]
# 将指定目录托管给指定urls.py文件的URL模式列表生成的模式集
from django.conf.urls import include
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
# 将指定目录托管给指定urls.py文件的URL模式列表生成的模式集
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('blog/', include('blog.urls')),
]



# 载入配置中的设置，本质仍然载入当前项目的settings.py
from django.conf import settings
from django.conf.urls.static import static
# 静态文件目录配置
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

