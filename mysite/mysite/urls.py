from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('summarizer/', include('summarizer.urls')),
    path('admin/', admin.site.urls),
]
