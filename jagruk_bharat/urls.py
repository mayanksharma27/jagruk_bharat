"""jagruk_bharat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/signUp/',views.userApiView.as_view()),
    url(r'login/',views.login,name='Login '),
    url(r'^api/data/',views.dataApiView.as_view()),
    url(r'^api/accountusers/(?P<state>[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12})/$',views.dataApiView.as_view()),
    url(r'^api/getData/',views.getData),
    url(r'^api/project',views.projectApiView.as_view()),
    url(r'^$',views.indexApiView),
    url(r'^dataEntry/',views.dataEntryApiView),
    url(r'^register/', views.registerApiView),
]
