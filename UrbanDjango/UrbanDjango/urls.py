from django.contrib import admin
from django.urls import path
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index5/', sign_up_by_django),
    path('', sign_up_by_html),
]
