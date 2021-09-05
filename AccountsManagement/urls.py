from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

def toadmin(request):
    return redirect('/ad')

urlpatterns = [
    path('', toadmin),
    path('ad/', admin.site.urls),
    path('transection/', include('transection.urls',namespace='transection')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header  =  "Account Management"  
admin.site.site_title  =  "Account Management site"
admin.site.index_title  =  "Account Management Admin"


