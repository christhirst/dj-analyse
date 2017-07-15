"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from . import views
from . import plots
from django.conf import settings
from django.conf.urls.static import static


app_name = 'analyse'

urlpatterns = [
    # /analyse/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/album/add
    url(r'add/$', views.DataCreate.as_view(), name='add'),
    url(r'^table/(?P<file_name>.+)', views.DataAnalyse, name='table'),
    url(r'^graph/charts/(?P<file_name>.+).png', plots.showimage),
    url(r'^graph/$', views.DataAnalyse, name='graph'),
    url(r'^graph/(?P<file_name>.+)', views.Graph, {'toggle': '1'}, name='graph'),
    # /music/album/delete
    url(r'(?P<pk>[0-9]+)/delete/', views.DataDelete.as_view(), name='data-delete'),
    # /music/album/edit
    url(r'^submit/(?P<file_name>.+)', views.DataEdit, name='data-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
