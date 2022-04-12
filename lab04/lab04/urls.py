from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('elecciones/', include('elecciones.urls')),
    path('admin/', admin.site.urls),
]
