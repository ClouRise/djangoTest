from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('second/', include('main.urls')),
    path('info/', include('info.urls')),
]
