from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import page

urlpatterns = [
	url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
	url(r'^$', page, name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
