"""online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from online.settings import MEDIA_ROOT
from users.views import IndexView, RegisterView, ActiveUserView, LoginView, LogoutView, ForgetPwdView, ResetView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^login/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),  # 参数变量是否可以设置为可有可无呢？
    url(r'^reset/$', ResetView.as_view(), name="reset_pwd"), # 接受请求为 http://ip/reset/?code=1212

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 富文本相关url
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]
