from django.conf.urls import url

from subtitle_app.models import Document
from . import views
from django.conf import settings
from django.conf.urls.static import static
files = Document.objects.all()
urlpatterns = [
    url(r'^$', views.model_form_upload, name='model_form_upload'),

    url(r'trans/(?P<pk>\d+)/$', views.translate, name='trans'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
