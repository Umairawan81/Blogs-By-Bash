
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog_Website.urls')),
    path('tinymce/',include('tinymce.urls'))
]
