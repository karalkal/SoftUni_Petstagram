from django.contrib import admin
from django.urls import path, include

import SoftUni_Petstagram

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SoftUni_Petstagram.main_app.urls'))
]
