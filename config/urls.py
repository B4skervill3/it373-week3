from django.contrib import admin
from django.urls import path, include
from pages import views as page_views

handler404 = 'pages.views.page_not_found_view'
handler500 = 'pages.views.server_error_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
