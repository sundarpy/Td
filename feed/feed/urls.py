from django.conf.urls import url
from django.contrib import admin
from appes import views
from appes.views import HomeView, MyfeedView, FacetedSearchView, autocomplete
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^myfeed/(?P<slug>[\w-]+)/$', MyfeedView.as_view(), name='myfeed'),
    url(r'^search/autocomplete/$', autocomplete),
    url(r'^find/', FacetedSearchView.as_view(), name='haystack_search'),
    
] + static(MEDIA_URL, document_root=MEDIA_ROOT)