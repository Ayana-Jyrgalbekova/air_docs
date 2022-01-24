from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from airdocs import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', DocsCreate.as_view(), name='create'),
    path('home/', DocsList.as_view(), name='home'),
    path('detail/<int:pk>/', DocsDetail.as_view(), name='detail'),
    path('category/<int:pk>/', CategoryFilter.as_view(), name='category'),
    path('workers/', Workers.as_view(), name='workers'),
    path('update/<int:pk>/', DocsUpdate.as_view(), name='update')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
