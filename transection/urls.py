from django.urls import path
from .views import MassUploadTransections

app_name = 'transection'
urlpatterns = [
    path('massupload/', MassUploadTransections.as_view() ,name='massupload' ),
]
