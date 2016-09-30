from django.conf.urls import include, url
from potholes.views import MapSearchView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', MapSearchView.as_view(), name='search')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

