from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Seed Pink Panel"
admin.site.site_title = "Seed Pink Admin Portal"
admin.site.index_title = "Welcome to Seed Pink Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("SeedPinkApp.urls")),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, 
                                 document_root=settings.MEDIA_ROOT)

