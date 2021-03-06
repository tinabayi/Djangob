from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^new/profile$', views.profile, name='profile'),
    url(r'^view/profile$', views.viewprofile, name='viewprofile'),
     url(r'^new/comment$', views.comments, name='comments')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

