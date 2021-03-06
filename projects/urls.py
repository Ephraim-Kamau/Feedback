from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.projects_today,name='projectsToday'),
    url(r'^search/', views.search_results, name='search_results'), 
    url(r'^profile/', views.profile, name='profile'), 
    url(r'new/profile$',views.new_profile,name='new_profile'),
    url(r'new/topic$',views.new_topic,name='new_topic'),
    url(r'topic/always',views.always_topic,name='always_topic'),
    url(r'comment',views.comment,name='comment'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)