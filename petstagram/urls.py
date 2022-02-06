from django.contrib import admin
from django.urls import path, include

import petstagram

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.main_app.urls'))
]
