from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'


from django.conf.urls import url
from . import views

urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),
    # login / logout urls


    url(r'^$', views.projectslist,name='project'),
]