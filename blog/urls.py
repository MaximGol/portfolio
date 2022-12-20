
from django.urls import path

from . import views
from django.contrib import admin

urlpatterns = [

    path('', views.all_blogs, name='all_blogs' ),
    path('admin/', admin.site.urls),

]