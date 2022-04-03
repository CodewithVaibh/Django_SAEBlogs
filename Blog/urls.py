from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SAEblogs.urls'))
]

admin.site.site_header = "SAE BLOGS"
admin.site.index_title = "Welcome to SAE BLOGS"
admin.site.site_title = "SAEblogs Website"