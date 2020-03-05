from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lessons/', include('lessons.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('markdownx/', include('markdownx.urls')),
    path('martor/', include('martor.urls')),
    path('boards/', include('boards.urls')),
    path('', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)