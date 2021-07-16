
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "icoder"
admin.site.site_tile = "icoder"
admin.site.index_title = "welcome to icoder admin pannel"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
]
