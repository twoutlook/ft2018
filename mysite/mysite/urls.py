from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # url(r'^uploadfileapp/', include('uploadfile.urls')),

    path('', include('polls.urls')),
]
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
