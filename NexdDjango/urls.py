
from django.contrib import admin
from django.urls import re_path, include
from django.views.generic import TemplateView
#Sets urls for main website
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('MovieApp/',include('MovieApp.urls')),
    re_path('', TemplateView.as_view(template_name='index.html')),
    
]
